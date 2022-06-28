from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response





@api_view(['POST'])
def Login_api(request):
    serializer = AuthTokenSerializer(data = request.data)
    serializer.is_valid(raise_exception = True)
    user = serializer.validated_data['user']
    _, token = AuthToken.objects.create(user)
    return Response({
        "user_info":{
            "id":user.id,
            "username":user.username,
            "email":user.email    
        },
        
        "token":token        
    })
    
    


@api_view(['GET'])
def get_user_data(request):
    user = request.user 
    if user.is_authenticated:
        return Response({
            
            'user_info':{
                'id':user.id,
            'username':user.username,
            'email':user.email    
                
            },
            
        })
        
    return Response({"error":"not authenticated"}, status = 400)
    
    


@api_view(['POST'])
def register_api(request):
    serializer = RegisterSerializer(data = request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.save()
    _, token = AuthToken.objects.create(user)
    
    return Response({
        
         "user_info":{
            "id":user.id,
            "username":user.username,
            "email":user.email    
        },
        
        "token":token        
    })
    





class ProfileView(APIView):
    def get(self, request, format = None):
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile, many=True)
        return Response(serializer.data)



class Project_Detail_View(APIView):
    def get(self, request, format = None):
        detail = Project_Details.objects.all()
        serializer = ProjectDetailsSerializer(detail, many=True)
        return Response(serializer.data)