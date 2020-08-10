from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='post_category')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.CharField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    category = models.ForeignKey(Category, on_delete=models.SET('Un-Categorised'), related_name='post_category')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
