from django.db import models

# Create your models here.

class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    def __str__(self):
        return self.site_name+ " : "+self.url

    class Meta:
        ordering = ['site_name']

#Todo : get_absolute_url

    def get_absolute_url(self):
        from django.urls import reverse
        # http://localhost:8000/bookmark/detail/4
        return reverse('bookmark:detail', args=[str(self.id)])