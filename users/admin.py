from django.contrib import admin
from .models import *


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('name','phone','email','location','project_id','profile_photo')
    search_fields=('phone','name')
    list_per_page=20
    

@admin.register(Project_Details)
class ProjectDetailsAdmin(admin.ModelAdmin):
    list_display=('project_detail','booking_amount','total_project_value','project_booking_date','paid_amount','remaining_amount','profile')
    search_fields=('paid_amounnt',)
    list_per_page=20

