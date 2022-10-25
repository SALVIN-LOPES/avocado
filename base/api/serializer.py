from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from base.models import Post, Profile, Company, JobOpening


# post serializer
class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

# user serializer
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email']

#profile serializer
class ProfileSerializer(ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = Profile
        fields = '__all__'

# company serializer
class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

# job opening serializer
class jobOpeningSerializer(ModelSerializer):
    class Meta:
        model = JobOpening
        fields = '__all__'



