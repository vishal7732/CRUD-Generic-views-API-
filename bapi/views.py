from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import Bookserializer
# Create your views here.


class Booklist(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = Bookserializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book
    serializer_class = Bookserializer