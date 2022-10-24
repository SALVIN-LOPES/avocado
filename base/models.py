
from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
    # user = models.ForeignKey(User,on_delete = models.CASCADE)
    name = models.CharField(max_length = 200,null=True,blank =True)
    website = models.CharField(max_length=200,null=True,blank =True)
    boi = models.TextField(null=True,blank =True)
    # linkedin = 
    # twitter = 
    # logo = 

    def __str__(self):
        return str(self.name)


class Social(models.Model):
    icon = models.ImageField(default = '',upload_to = '', blank=True, null=True)
    link = models.CharField(max_length = 200, blank=True, null=True)


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    avatar = models.ImageField(default = '',upload_to = '', blank=True, null=True)
    name = models.CharField(max_length = 200,null=True,blank=True,default='TEST' )
    socials = models.ManyToManyField('Social',blank=True)
    skills = models.ManyToManyField('Skill',blank=True)
    verified = models.BooleanField(default = False)
    
    def __str__(self):
        return str(self.user.username)

class Skill(models.Model):
    name = models.CharField(max_length = 200,blank=True, null=True)
    link = models.CharField(max_length = 200, blank=True, null=True)


class Review(models.Model):
    owner = models.ForeignKey(User,on_delete = models.CASCADE,null=True,blank=True)
    body = models.TextField(null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.body[0:40])
    
    
class Post(models.Model):

    OPTIONS = (
        ('collab','collab'),
        ('job','job'),
        ('default','default'),
    )

    owner = models.ForeignKey(User,on_delete = models.CASCADE,null=True,blank=True)
    body = models.TextField(null=True,blank=True)
    likes = models.ManyToManyField(User,related_name="likes",blank = True)
    post_type = models.CharField(choices=OPTIONS,default=OPTIONS[2],max_length=1000)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.body[0:50])
    
class Comment(models.Model):
    owner = models.ForeignKey(User,on_delete = models.CASCADE,null=True,blank=True)
    body = models.TextField(blank = True,null=True)
    post = models.ForeignKey(Post,on_delete = models.CASCADE,blank=True, null=True)
    created = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.body[0:50])
