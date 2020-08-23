from django.contrib import admin
from .models import Employee
from django.contrib.auth.models import Group

# Register your models here.
admin.site.register(Employee)
admin.site.site_header = 'ABC Admin Panel'
admin.site.unregister(Group)
