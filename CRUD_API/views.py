from rest_framework import generics
from .models import Person
from .serializers import PersonSerializer


class CreateView(generics.CreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class ReadView(generics.RetrieveAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = 'id'


class UpdateView(generics.UpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = 'id'


class DeleteView(generics.DestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = 'id'
