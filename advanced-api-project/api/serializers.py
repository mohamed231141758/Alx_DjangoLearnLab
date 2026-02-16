from rest_framework import serializers
from .models import Author, Book
from datetime import date

# BookSerializer - serializes all fields of the Book model
# Also handles custom validation for publication_year
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Custom validation to ensure publication_year is not in the future
    def validate_publication_year(self, value):
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError(
                f"Publication year cannot be in the future. Current year is {current_year}."
            )
        return value

# AuthorSerializer - serializes the Author model
# Includes a nested BookSerializer to show all books by this author
class AuthorSerializer(serializers.ModelSerializer):
    # Nested serializer - shows full book details for each book by this author
    # many=True because one author can have many books
    # read_only=True because we don't want to create books through author
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
