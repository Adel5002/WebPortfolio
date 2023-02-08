from django.db import models

class PortfolioStructure(models.Model):
    title = models.CharField(max_length=255, unique=True)
    upload_img = models.ImageField(upload_to='image/%Y/%m/%d/', blank=True)
    upload = models.FileField(upload_to='video/%Y/%m/%d/')
    descr = models.TextField()
    site_url = models.URLField(blank=False)
    git_url = models.URLField(blank=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']

