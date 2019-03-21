from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(max_length=256, blank=True)

    def __str__(self):
        return self.name


class URLText(models.Model):
    url = models.URLField(max_length=256, )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    upload_date = models.DateTimeField(auto_now=True)   # zmiana rekordu może wynikać tylko z ponownego uploadu

    class Meta:
        ordering = ['url', 'category']

    def __str__(self):
        return f"Text from: {self.url}, saved on: {self.upload_date}"

# Upload directory for photos
def cat_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/cat_<id>/<filename>
    return f'cat_{instance.category.id}/{filename}'


class Photo(models.Model):
    path = models.ImageField(max_length=128, upload_to=cat_directory_path)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(max_length=256, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Photo file: {self.path}'
