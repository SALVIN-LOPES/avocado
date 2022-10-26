from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializer import PostSerializer,ProfileSerializer,CompanySerializer,jobOpeningSerializer
from django.contrib.auth.models import User
from base.models import Post, Profile, Company,JobOpening

from base.api import serializer

@api_view(['GET'])
def getRoutes(request):
    routes = {
        'getRoutes':'',
        'getUsers':'/api/users',
        'getUser':'/api/users/<str:username>/',
        'Recommended Users':'/api/users/recommended/',

        'get companies':'api/companies/',
        'get Company': 'api/company/<str:pk>/',

        'addPosts':'/api/posts', # post request
        'getPosts':'/api/posts', # get request
        'getPost':'/api/posts/<str:pk>/', # get request
        'updatePosts':'/api/posts/<str:pk>/update/',
        'deletePosts':'/api/posts/<str:pk>/delete/',
        

    }
    return Response(routes)

@api_view(['GET'])
def getPosts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts,many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getPost(request,pk):
    post = Post.objects.filter(id=pk).first()
    serializer = PostSerializer(post,many=False)

    return Response(serializer.data)

# add a post
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addPost(request):
    data = request.data
    user = request.user
    print("DATA:",data)
    post = Post.objects.create(
        owner=user,
        body = data['body'],
    )
    serializer = PostSerializer(post,many=False)

    return Response({ 'message':"post created successfully" ,"data":serializer.data})

# update a post
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updatePost(request,pk):
    data = request.data
    user = request.user
    print("DATA:",data)
    post = Post.objects.filter(id=pk).first()
    post.body = data['body']
    post.save()

    serializer = PostSerializer(post,many=False)

    return Response({ 'message':"post updated successfully" ,"data":serializer.data})

# delete a post
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deletePost(request,pk):
    post = Post.objects.filter(id=pk).first()
    print(post.owner,request.user.id)
    if post.owner == request.user:

        post = post.delete()
        serializer = PostSerializer(post,many=False)

        return Response({ 'message':"post deleted successfully" ,"data":serializer.data})
    return Response({ 'message':"you are not authorized to delete the post"})


@api_view(['GET'])
def getUsers(request):
    users = Profile.objects.all()
    serializer = ProfileSerializer(users,many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getRecommendedUsers(request):
    users = Profile.objects.filter(verified = True).order_by("?")[0:10]
    serializer = ProfileSerializer(users,many=True)

    return Response(serializer.data)

@api_view(['GET'])
def getUser(request,username):
    user = Profile.objects.filter(user__username = username).first()
    serializer = ProfileSerializer(user,many=False)

    return Response(serializer.data)

# get companies
@api_view(['GET'])
def getCompanies(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies,many=True)

    return Response(serializer.data)
    
# get company
@api_view(['GET'])
def getCompany(request,pk):
    company = Company.objects.filter(id=pk).first()
    serializer = CompanySerializer(company,many=False)

    return Response(serializer.data)

@api_view(['GET'])
def getLatestJobs(request):
    jobs = JobOpening.objects.all().order_by('-created')[0:10]
    serializer = jobOpeningSerializer(jobs,many=True)

    return Response(serializer.data)
