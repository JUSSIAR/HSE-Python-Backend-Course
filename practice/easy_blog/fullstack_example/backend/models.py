from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.CharField(max_length=100, null=True)


class Comment(models.Model):
    text = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.CharField(max_length=100, null=True)
