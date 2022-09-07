from rest_framework import serializers
from .models import book


class book_serializer(serializers.ModelSerializer):

    class Meta:
        model = book
        fields = ('id', 'name', 'isbn', 'authors', 'number_of_pages',
                  'publisher', 'country', 'release_date')
