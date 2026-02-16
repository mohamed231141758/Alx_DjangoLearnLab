from django.db import models
from django.contrib.auth.models import User

# Post model - represents a blog post
class Post(models.Model):
    # Title of the blog post
    title = models.CharField(max_length=200)
    # Main content of the blog post
    content = models.TextField()
    # Date and time when the post was published (set automatically)
    published_date = models.DateTimeField(auto_now_add=True)
    # Author of the post - linked to Django's built-in User model
    # One author can have many posts
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_date']
