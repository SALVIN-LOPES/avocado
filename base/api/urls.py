from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.getRoutes,name = 'getRoutes'),
    path('posts/add/',views.addPost,name='addPost'),
    path('posts/<str:pk>/',views.getPost,name='getPost'),
    path('posts/<str:pk>/update/',views.updatePost,name='updatePost'),
    path('posts/<str:pk>/delete/',views.deletePost,name='deletePost'),
    path('posts/',views.getPosts,name='getPosts'),

    path('users/',views.getUsers,name='getUsers'),
    path('users/recommended/',views.getRecommendedUsers,name='getRecommendedUsers'),
    path('users/<str:username>/',views.getUser,name='getUser'),

    path('companies/',views.getCompanies,name='getCompanies'),
    path('company/<str:pk>/',views.getCompany,name='getCompany'),

    path('jobOpenings/',views.getLatestJobs,name='jobOpening')


]