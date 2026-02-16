from django.urls import path
from . import views

urlpatterns = [
    # List all books - open to all users
    path('books/', views.BookListView.as_view(), name='book-list'),

    # Get a single book by ID - open to all users
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),

    # Create a new book - authenticated users only
    path('books/create/', views.BookCreateView.as_view(), name='book-create'),

    # Update a book - authenticated users only
    path('books/<int:pk>/update/', views.BookUpdateView.as_view(), name='book-update'),

    # Delete a book - authenticated users only
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book-delete'),
]
