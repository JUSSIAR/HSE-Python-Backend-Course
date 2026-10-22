from django.db import models


class Article(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    id = models.IntegerField(primary_key=True)
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    author = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.content
