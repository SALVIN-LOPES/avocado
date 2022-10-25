from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.getRoutes,name = 'getRoutes'),
    path('post/<str:pk>/',views.getPost,name='getPost'),
    path('posts/',views.getPosts,name='getPosts'),
    path('addPost/',views.addPost,name='addPost'),

    path('users/',views.getUsers,name='getUsers'),
    path('users/recommended/',views.getRecommendedUsers,name='getRecommendedUsers'),
    path('users/<str:username>/',views.getUser,name='getUser'),

    path('companies/',views.getCompanies,name='getCompanies'),
    path('company/<str:pk>/',views.getCompany,name='getCompany'),

    path('jobOpenings/',views.getLatestJobs,name='jobOpening')


]