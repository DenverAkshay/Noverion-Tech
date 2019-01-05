from django.contrib import admin
from geoposition.fields import GeopositionField
from .models import Tenant
# Register your models here.

class TenantAdmin(admin.ModelAdmin):
    list_display = ('name','age','gender','slug','mobile_1','mobile_2','mobile_3','address','city','country','created_on','location',)
    list_filter = ('city','country')
    search_fields = ('name','age','gender','created_on','slug','address','city','country','mobile_1','mobile_2','mobile_3')
    prepopulated_fields = {'slug':('name',)}

    list_editable = ('age','gender','created_on')



admin.site.register(Tenant,TenantAdmin)
