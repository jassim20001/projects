from django.urls import path
from .views import *
from . import views

urlpatterns =[
    path('',MyStorey.as_view(),name='storey'),
    path('blogs',MyBlogs.as_view(),name='blogs'),
    path('comments',MyComment.as_view(),name='comments'),
   

]
