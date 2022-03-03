from django.urls import path
from . import views
from FItnessStatus.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static


urlpatterns = [
    path('<id>/', views.DeleteBlog, name='delete'),

]
urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)