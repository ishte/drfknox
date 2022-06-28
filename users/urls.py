from django.urls import path
from knox import views as knox_views
from . import views
from .views import *




urlpatterns = [
    path('login/', views.Login_api),
    path('user/', views.get_user_data),
    path('register/', views.register_api),
    path('logout/', knox_views.LogoutView.as_view()),
    path('logoutall/', knox_views.LogoutAllView.as_view()),
    path('profile/', views.ProfileView.as_view() ),
    path('projectdetail/',views.Project_Detail_View.as_view())
    
    
    
    
]
