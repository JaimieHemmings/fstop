from django.contrib import admin
from blog.models import Article
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    pass

class ArticleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Message, MessageAdmin)
admin.site.register(Article, ArticleAdmin)
