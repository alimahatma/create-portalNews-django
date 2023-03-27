from django.contrib import admin
from .models import Category, News, Comment

admin.site.register(Category) 


class AdminNews(admin.ModelAdmin):
    list_display=('title','category','add_time','author')

admin.site.register(News, AdminNews)

class AdminComment(admin.ModelAdmin):
    list_display=('status','news','email','comment')

admin.site.register(Comment, AdminComment)
