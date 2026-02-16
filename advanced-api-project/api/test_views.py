from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import Author, Book

class BookAPITestCase(APITestCase):
    """
    Test suite for the Book API endpoints.
    Tests CRUD operations, filtering, searching, ordering,
    and authentication/permission controls.
    """

    def setUp(self):
        """Set up test data before each test."""
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

        # Create a token for the test user
        self.token = Token.objects.create(user=self.user)

        # Set up authenticated client
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Create test author
        self.author = Author.objects.create(name="George Orwell")

        # Create test book
        self.book = Book.objects.create(
            title="1984",
            publication_year=1949,
            author=self.author
        )

        # Define URLs
        self.list_url = '/api/books/'
        self.create_url = '/api/books/create/'
        self.detail_url = f'/api/books/{self.book.pk}/'
        self.update_url = f'/api/books/{self.book.pk}/update/'
        self.delete_url = f'/api/books/{self.book.pk}/delete/'

    # ==================== LIST TESTS ====================

    def test_list_books_authenticated(self):
        """Test that authenticated users can list all books."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("✅ List books (authenticated): PASSED")

    def test_list_books_unauthenticated(self):
        """Test that unauthenticated users can also list books (read-only)."""
        self.client.credentials()
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("✅ List books (unauthenticated): PASSED")

    # ==================== CREATE TESTS ====================

    def test_create_book_authenticated(self):
        """Test that authenticated users can create a book."""
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'Animal Farm',
            'publication_year': 1945,
            'author': self.author.id
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        print("✅ Create book (authenticated): PASSED")

    def test_create_book_unauthenticated(self):
        """Test that unauthenticated users cannot create a book."""
        self.client.credentials()
        data = {
            'title': 'Animal Farm',
            'publication_year': 1945,
            'author': self.author.id
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        print("✅ Create book (unauthenticated blocked): PASSED")

    def test_create_book_future_year(self):
        """Test that books with future publication year are rejected."""
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'Future Book',
            'publication_year': 2099,
            'author': self.author.id
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        print("✅ Create book (future year rejected): PASSED")

    # ==================== UPDATE TESTS ====================

    def test_update_book_authenticated(self):
        """Test that authenticated users can update a book."""
        self.client.force_authenticate(user=self.user)
        data = {
            'title': '1984 Updated',
            'publication_year': 1949,
            'author': self.author.id
        }
        response = self.client.put(self.update_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("✅ Update book (authenticated): PASSED")

    def test_update_book_unauthenticated(self):
        """Test that unauthenticated users cannot update a book."""
        self.client.credentials()
        data = {
            'title': '1984 Updated',
            'publication_year': 1949,
            'author': self.author.id
        }
        response = self.client.put(self.update_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        print("✅ Update book (unauthenticated blocked): PASSED")

    # ==================== DELETE TESTS ====================

    def test_delete_book_authenticated(self):
        """Test that authenticated users can delete a book."""
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
        print("✅ Delete book (authenticated): PASSED")

    def test_delete_book_unauthenticated(self):
        """Test that unauthenticated users cannot delete a book."""
        self.client.credentials()
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        print("✅ Delete book (unauthenticated blocked): PASSED")

    # ==================== FILTER/SEARCH/ORDER TESTS ====================

    def test_filter_books_by_title(self):
        """Test filtering books by title."""
        response = self.client.get(self.list_url, {'title': '1984'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("✅ Filter books by title: PASSED")

    def test_search_books(self):
        """Test searching books by title."""
        response = self.client.get(self.list_url, {'search': '1984'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("✅ Search books: PASSED")

    def test_order_books_by_title(self):
        """Test ordering books by title."""
        response = self.client.get(self.list_url, {'ordering': 'title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("✅ Order books by title: PASSED")

    def test_order_books_by_publication_year(self):
        """Test ordering books by publication year."""
        response = self.client.get(self.list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("✅ Order books by publication year: PASSED")
