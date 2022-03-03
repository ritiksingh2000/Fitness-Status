from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings 
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.Home, name='home'),
    path('contact', views.contact, name='contact'),
    path('contactus', views.Contactus, name='contactus'),
    path('bmi', views.bmi, name='bmi'),
    path('subs', views.subs, name='subs'),
    path('calorie', views.Calorie, name='calorie'),
    path('healthtube', views.videos, name='healthtube'),
    path('share', views.ShareVideo, name='share'),
    path('all_blogs', views.Blog, name='blogs'),
    path('blog/<id>/', views.Blogpage, name='blogpage'),
    path('profile', views.Profile, name='profile'),
    path('createcatgry', views.CreateCategory, name='createcatgry'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('login', views.login, name='login'),
    path('regestration', views.regestration, name='regestration'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)