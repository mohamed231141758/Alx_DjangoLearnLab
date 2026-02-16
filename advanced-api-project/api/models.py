from django.db import models

# Author model - stores information about book authors
class Author(models.Model):
    # Name field to store the author's full name
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Book model - stores information about books
# Each book is linked to one Author (one-to-many relationship)
class Book(models.Model):
    # Title of the book
    title = models.CharField(max_length=200)
    # Year the book was published
    publication_year = models.IntegerField()
    # Foreign key linking book to its author
    # If author is deleted, all their books are deleted too
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
