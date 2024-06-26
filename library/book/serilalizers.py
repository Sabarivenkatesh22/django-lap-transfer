from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['ISBN', 'title', 'author', 'publication_date', 'description', 'genre']
        extra_kwargs = {
            'description': {'required': False},
            'genre': {'required': False}
        }