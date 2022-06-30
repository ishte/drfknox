from asyncore import read
from dataclasses import fields
from rest_framework import serializers 
from .models import *
from django.contrib.auth.models import User
from rest_framework import serializers, validators

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password','email','first_name','last_name')
        
        extra_kwargs = {
            "passsword":{'write_only':True},
            "email":{
                "required":True,
                "allow_blank":False,
                "validators":{
                    validators.UniqueValidator(
                        User.objects.all(), " A user with that Email already exist"
                    )
                }
            }
        }
        
        
        def create(self, validated_data):
            username = validated_data.get('username')
            password = validated_data.get('password')
            email = validated_data.get('email')
            first_name = validated_data.get('first_name')
            last_name = validated_data.get('last_name')
            
            user = User.objects.create(
                username = username,
                password = password,
                email = email,
                first_name = first_name,
                last_name = last_name
                
            )
            return user
            





class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
        


class PaymentTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment_Tracking
        fields = ('installment_number',)
        



class ProjectDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project_Deatails
        fields = ("project_detail",)


class ProjectDetailsSerializer(serializers.ModelSerializer):
    project_details =  ProjectDetailsSerializer(read_only=True,many=True) 
    payment_tracking = PaymentTrackingSerializer(read_only=True,many=True)                  
    class Meta:
           model   =  User
           fields  = ['id','username','payment_tracking','project_details']              


