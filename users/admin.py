from django.contrib import admin
from .models import *


admin.site.register(Profile)
admin.site.register(Project_Deatails)
admin.site.register(Payment_Tracking)




# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display=('name','phone','email','location','project_id','profile_image')
#     search_fields=('phone','name')
#     list_per_page=20
    

# @admin.register(Project_Deatails)
# class ProjectDetailsAdmin(admin.ModelAdmin):
#     list_display=('project_detail','booking_amount','total_project_value','project_booking_date','paid_amount','remaining_amount','profile')
#     search_fields=('paid_amounnt',)
#     list_per_page=20



# @admin.register(Payment_Tracking)
# class PackageAdmin(admin.ModelAdmin):
#     list_display=('id','user','total_project_value','total_paid','due_amount','payment_mode')
#     fields=('user','total_project_value','total_paid','payment_mode')
#     search_fields = ('user__username',)
#     list_per_page=10
    
    
    

# @admin.register()
# class ProjectTrackerAdmin(admin.ModelAdmin):
#     list_display=('id','username','project','clinet_meeting','planning','design_ui_ux','analysis','manipulation','testing','maintenance','handover')
#     search_fields=('planning',)
#     list_per_page=20
    