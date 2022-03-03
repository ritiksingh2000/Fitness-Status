from django.shortcuts import render,redirect
from django.contrib import messages
from Fitness_Status.models import Article
# Create your views here.
def DeleteBlog(request, id):
    blog = Article.objects.get(id=id)
    blog.delete()

    messages.info(request,"Blog Successfully Deleted.")
    return redirect('profile')