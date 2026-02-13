from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),         
    path('allposts/', views.blogposts, name='allposts'),
    # path('allposts/python-intro', views.python_intro),
    # path('allposts/django-basics', views.django_basics),
    # path('allposts/python-oops', views.python_oops),
    path('allposts/<slug:blog>', views.blogs_post, name='blog-post'),   #'blog-post' is a URL name
]
