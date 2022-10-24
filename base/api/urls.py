from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.home_api,name = 'home_api'),
    
]