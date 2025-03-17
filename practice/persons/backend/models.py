from django.db import models


class Person(models.Model):
    first_name = models.TextField(max_length=500, blank=True)
    last_name = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return 'Person {}'.format(self.first_name)
