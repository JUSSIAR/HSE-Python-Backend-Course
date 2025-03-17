from rest_framework import viewsets

from backend import models as backend_models
from backend import serializers


class PersonsAPIViewSet(viewsets.ModelViewSet):
    queryset = backend_models.Person.objects.all()
    serializer_class = serializers.PersonSerializer
