from urllib import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status





@api_view(['POST'])
def Login_api(request):
    serializer = AuthTokenSerializer(data = request.data)
    serializer.is_valid(raise_exception = True)
    user = serializer.validated_data['user']
    _, token = AuthToken.objects.create(user)
    profile = Profile.objects.filter().first()
    user_and_porject_details = ProjectDetailsSerializer(user)
    # print("ksnhfksdf")
    print(user_and_porject_details.data)
    return Response({
        "user_info":{
            "id":user.id,
            "username":user.username,
            "email":user.email,
            "project_detail": user_and_porject_details.data
        },
        
        "token":token        
    })
    #return Response(data="shv")

    


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
    







class Profille_List(APIView):
    def get(self,request):
        try:
            id=request.GET.get('id')
            if id is not None:
                obj = Profile.objects.filter(id=id).first()
                if obj is not None:
                    serializer=ProfileSerializer(obj)
                    return Response(data=serializer.data,status=status.HTTP_200_OK)
                else:
                    return Response({'message':'Id not found'},status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'message':'Id is blank'},status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'message':'Something went wrong'},status=status.HTTP_400_BAD_REQUEST)
        
        
        
    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
        
        
        
    


class Project_detail_view(APIView):
    def get(self,request):
        try:
            id=request.GET.get('id')
            if id is not None:
                obj=Project_Deatails.objects.filter(id=id).first()
                if obj is not None:
                    serializer = ProjectDetailsSerializer(obj)
                    return Response(data=serializer.data,status=status.HTTP_200_OK)
                else:
                    return Response({'message':'Id not found'},status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'message':'Id is blank'},status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'message':'Something went wrong'},status=status.HTTP_400_BAD_REQUEST)
        
    
    def post(self, request):
        serializer = ProjectDetailsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    
    
    
    
    