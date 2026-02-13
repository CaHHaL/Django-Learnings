from django.contrib import admin

# Register your models here.
from .models import Post,Author,Tag




class PostAdmin(admin.ModelAdmin):
    list_filters=['author','tag','date']
    list_display=['title','date','author']
    
    
admin.site.register(Post,PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)