from django.contrib import admin

# Register your models here.
from article.models import ArticlePost, ArticleColumn

admin.site.register(ArticlePost)
admin.site.register(ArticleColumn)