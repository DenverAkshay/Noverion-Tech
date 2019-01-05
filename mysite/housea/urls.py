from django.urls import path
from .models import Tenant
from .  import views
from .views import (CreateTenant,TenantDetail,EditTenant,DeleteTenant)
from django.contrib.auth import views as auth_views

urlpatterns= [
    path('',views.home,name='home'),
    path('login/',views.user_login,name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='housea/logout.html'),name='logout'),
    path('tenant/new/',views.CreateTenant.as_view(),name='create-tenant'),
    path('tenant/<int:id>/<str:slug>/',views.TenantDetail.as_view(),name='tenant-detail'),
    path('tenant/<int:id>/<str:slug>/edit/',views.EditTenant.as_view(),name='tenant-edit'),
    path('tenant/<int:id>/<str:slug>/delete/',views.DeleteTenant.as_view(),name='tenant-delete'),
]
