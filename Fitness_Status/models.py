from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# HOME
class Subs(models.Model):
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

class VideoCategory(models.Model):
    Category = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.Category

class Healthtube(models.Model):
    Video_Name = models.CharField(max_length=100)
    Video_Link = models.CharField(max_length=500)
    Channel_Name = models.CharField(max_length=100)
    Channel_Link = models.CharField(max_length=500)
    category = models.ForeignKey(VideoCategory, on_delete=models.CASCADE)
    Added_By = models.CharField(max_length=150, blank=True, null=True)
    Description = models.TextField()
    Date = models.DateTimeField(auto_now_add=True)

class UserMessage(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Date = models.DateTimeField(auto_now_add=True)
    Subject = models.CharField(max_length=200)
    Message = models.TextField()

    def __str__(self):
        return self.Name + self.Subject


class VideoSuggestion(models.Model):
    Channel_Name = models.CharField(max_length=100)
    Channel_Link = models.CharField(max_length=100)
    Video_Name = models.CharField(max_length=100)
    Video_Link = models.CharField(max_length=100)
    Category = models.CharField(max_length=100)
    Added_By = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Added_By + self.Channel_Name


# ARTICLES
class Categories(models.Model):
    category = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category


class Article(models.Model):
    title = models.CharField(max_length=100, unique=True, )
    author = models.CharField(max_length=50)
    author_email = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    thumbnail = models.FileField(upload_to='blog/')
    body = RichTextField()


    def limit(self):
        return self.body[:200] + '....'

    def __str__(self):
        return self.title + ' | ' + str(self.author)



