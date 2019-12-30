from django.urls import path
from django.views.generic import ListView
from . import views
from home.models import Post

urlpatterns = [
	path('', views.index, name='index'),
	path('contact/', views.contact, name='contact'),
	path('about/', views.about, name="about"),
	path('', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25], template_name="home/homepage.html")),

]