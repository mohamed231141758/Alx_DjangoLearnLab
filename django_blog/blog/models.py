from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Post model - represents a blog post
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    # Tags - many-to-many relationship using django-taggit
    tags = TaggableManager()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_date']

# Comment model - represents a comment on a blog post
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'

    class Meta:
        ordering = ['created_at']
