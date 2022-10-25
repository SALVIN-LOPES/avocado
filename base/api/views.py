from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import PostSerializer,ProfileSerializer,CompanySerializer,jobOpeningSerializer
from django.contrib.auth.models import User
from base.models import Post, Profile, Company,JobOpening

from base.api import serializer

@api_view(['GET'])
def getRoutes(request):
    routes = {
        'users':'/api/users',
        'posts':'/api/posts',

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
@api_view(['GET'])
def addPost(request):
    data = request.data
    # Post.objects.create(
    #     "owner" : request.user,
    #     "body" :
    #     "likes" :
    #     "post_type":
        
    # )
    return Response('Post was added!!')

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
