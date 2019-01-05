from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Tenant
from django.urls import reverse
from django.views.generic import (CreateView,DetailView,UpdateView,DeleteView)
from .forms import TenantCreateForm,TenantEditForm,UserLoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.db.models import Q
from django.contrib import messages

# Create your views here.
@login_required
def home(request):
    datas = Tenant.objects.all().order_by('-created_on')
    query = request.GET.get('q')
    if query:
        datas = Tenant.objects.filter(
            Q(name__icontains=query)|Q(age__icontains=query)|Q(gender__icontains=query)|Q(mobile_1__icontains=query)|
            Q(mobile_2__icontains=query)|Q(mobile_3__icontains=query)|Q(address__icontains=query)|Q(city__icontains=query)|
            Q(country__icontains=query)|Q(location__icontains=query)
        )
    context = {'datas': datas}
    return render(request,'housea/home.html',context)

class TenantDetail(DetailView):
    model = Tenant


class CreateTenant(CreateView):
    model = Tenant
    form_class = TenantCreateForm
    success_url="/"

class EditTenant(UpdateView):
    model = Tenant
    form_class = TenantEditForm
    template_name = 'housea/tenant_edit.html'

class DeleteTenant(DeleteView):
    model = Tenant
    success_url = '/'

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request,username=username,password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    messages.success(request,f'Login successful!')
                    return HttpResponseRedirect(reverse('home'))

            else:
                messages.error(request,f'User does not exist')
    else:
        form = UserLoginForm()
    context={
        'form':form
    }
    return render(request,'housea/login.html',context)
