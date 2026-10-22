from django.contrib import admin

from .models import Article
from .models import Comment

admin.site.register(Article)
admin.site.register(Comment)
