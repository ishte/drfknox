from django.db import models

class BaseModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)  
    class Meta:
        abstract=True
        
           
class Profile(BaseModel):
    name=models.CharField(max_length=100)
    phone=models.CharField(max_length=12)
    email=models.EmailField(max_length=20)  
    location=models.CharField(max_length=100)
    project_id=models.IntegerField()
    profile_photo=models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    def __str__(self):
        return self.name 
        

         
class Project_Details(BaseModel):
    project_detail=models.CharField(max_length=100)
    booking_amount=models.IntegerField()
    total_project_value=models.IntegerField() 
    project_booking_date=models.DateTimeField()
    paid_amount=models.IntegerField()
    remaining_amount=models.FloatField()
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE)
    def __str__(self):
        return self.project_detail


