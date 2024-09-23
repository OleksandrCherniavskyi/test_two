from django.db import models
from django.contrib.auth.models import User  # Import User model for author field
from django.utils.text import slugify

class Article(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Link article to user
    created_at = models.DateTimeField(auto_now_add=True)  # Automatic timestamp on creation
    slug = models.SlugField(unique=True, max_length=255, blank=True)  # Unique slug for URL

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)  # Generate slug from title on save
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title