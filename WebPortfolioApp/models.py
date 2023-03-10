from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class PortfolioStructure(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(null=True, unique=True, db_index=True)
    upload_img = models.ImageField(upload_to='image/%Y/%m/%d/', blank=True)
    upload = models.FileField(upload_to='video/%Y/%m/%d/')
    descr = models.TextField()
    site_url = models.URLField(blank=False)
    git_url = models.URLField(blank=False)
    likes = models.ManyToManyField(User, related_name='likes')

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('project', kwargs={'proj_slug': self.slug})

    class Meta:
        ordering = ['id']


class Comment(models.Model):
    project = models.ForeignKey(PortfolioStructure, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.project.title, self.name)




