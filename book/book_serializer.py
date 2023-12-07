from rest_framework import serializers

from book import models



class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ['id', 'name', 'description', 'authors', 'genre', 'publication_date', 'isbn', 'price']
        