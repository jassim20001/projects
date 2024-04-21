

# Create your views here.
from django.contrib import messages
from django.shortcuts import render

from .models import *
from .serlizer import *

from rest_framework import generics
class MyBlogs(generics.CreateAPIView):
    serializer_class=BlogSer
    queryset = Blog.objects.all()
class MyComment(generics.CreateAPIView):
    serializer_class=CommentSer
    queryset = Comment.objects.all()
class MyStorey(generics.CreateAPIView):
    serializer_class=StoreySer
    queryset = Storey.objects.all()