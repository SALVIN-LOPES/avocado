from django.contrib import admin

from .models import Company, Profile, Review,Social, Post,Skill, Comment

admin.site.register(Company)
# admin.site.register(JobOpening)
admin.site.register(Profile)
admin.site.register(Review)
admin.site.register(Social)
admin.site.register(Skill)
admin.site.register(Post)
admin.site.register(Comment)
