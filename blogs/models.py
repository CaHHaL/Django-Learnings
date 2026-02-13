from django.db import models

# Create your models here.


class Author(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Tag(models.Model):
    caption=models.CharField(max_length=20)
    def __str__(self):
        return f"{self.caption}"

class Post(models.Model):
    title=models.CharField(max_length=100)
    preview=models.TextField(max_length=500)
    image=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True)
    slug=models.SlugField(max_length=100,unique=True)
    content=models.TextField(max_length=2000)
    author=models.ForeignKey(Author,on_delete=models.SET_NULL,null=True)
    tag=models.ManyToManyField(Tag)
    def __str__(self):
        return f"{self.title }"
    
#python manage.py makemigrations
#python manage.py migrate    

