from django.db import models  
from django.contrib.auth.models import User
class BaseModel(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)  
    
    class Meta:
        abstract=True
        
         
class Profile(BaseModel):
    name=models.CharField(max_length=100)
    phone=models.TextField()
    email=models.EmailField(max_length=20)  
    location=models.CharField(max_length=100)
    project_id=models.IntegerField()
    profile_photo=models.ImageField(height_field=None, width_field=None, max_length=100)
    
    
     
    def __str__(self):
        return self.name 
        
        
class Project_Deatails(BaseModel):
    project_detail=models.CharField(max_length=100)
    booking_amount=models.IntegerField()
    total_project_value=models.IntegerField() 
    project_booking_date=models.DateTimeField()
    paid_amount=models.IntegerField()
    remaining_amount=models.IntegerField()
    user=models.ForeignKey(User,related_name="project_details",null=True,blank=True,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.project_detail


class Payment_Tracking(BaseModel):
    installment_number=models.IntegerField()
    date=models.DateField()
    reference_number=models.IntegerField()
    amount=models.IntegerField()    
    refund=models.IntegerField()
    project_deatails=models.ForeignKey(Project_Deatails, null=True,blank=True,on_delete=models.CASCADE)
    
    user=models.ForeignKey(User, related_name="payment_tracking",on_delete=models.CASCADE,null=True,blank=True)
    # def __str__(self):
        # return self.installment_number
    
  
