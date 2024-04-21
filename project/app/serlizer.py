from rest_framework import serializers
# from .models import post
from django.contrib.auth.models import User
from .models import *

class BlogSer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
        
class CommentSer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
class StoreySer(serializers.ModelSerializer):
    class Meta:
        model = Storey
        fields = '__all__'
