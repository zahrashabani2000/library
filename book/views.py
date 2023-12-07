from rest_framework import generics
from rest_framework import viewsets
from rest_framework.views import APIView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters 
from rest_framework.response import Response

from book import models
from book import book_serializer
from borrower import views


class BookList(generics.ListAPIView):
    """Retrive book list"""
    queryset = models.Book.objects.all()
    serializer_class = book_serializer.BookSerializer


class BookView(LoginRequiredMixin, viewsets.ModelViewSet):
    """After loing handle CRUD"""
    login_url = 'login'
    redirect_field_name = 'book-info'
    serializer_class = book_serializer.BookSerializer
    queryset = models.Book.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'authors', 'genre')
    

