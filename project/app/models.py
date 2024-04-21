from django.db import models

class Storey(models.Model):
    NameAuthor=models.CharField(max_length=100)
    Title=models.CharField(max_length=1000)
    NameStorey=models.CharField(max_length=5000)


class Comment(models.Model):
    comment=models.CharField(max_length=1000)

class Blog(models.Model):
    Title=models.CharField(max_length=1000)
    blog=models.CharField(max_length=5000)
