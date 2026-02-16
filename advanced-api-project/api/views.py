from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Book
from .serializers import BookSerializer

# ListView - retrieves all books
# Supports filtering, searching, and ordering
# Example usage:
#   Filter:  /api/books/?author=1&publication_year=1949
#   Search:  /api/books/?search=1984
#   Order:   /api/books/?ordering=title or ?ordering=-publication_year
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Filter backends for filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Fields that can be filtered by exact match
    filterset_fields = ['title', 'author', 'publication_year']

    # Fields that can be searched with text search
    search_fields = ['title', 'author__name']

    # Fields that can be used for ordering
    ordering_fields = ['title', 'publication_year']

    # Default ordering
    ordering = ['title']

# DetailView - retrieves a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# CreateView - adds a new book
# Only authenticated users can create books
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# UpdateView - modifies an existing book
# Only authenticated users can update books
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# DeleteView - removes a book
# Only authenticated users can delete books
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
