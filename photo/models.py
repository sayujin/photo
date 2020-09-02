from django.db import models
from django.urls import reverse
#장고의 기본 유저
from django.contrib.auth.models import User
# Create your models here.
class Photo(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_photos')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d', default='photos/no_image.png')
    text = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    #모델의 옵션들
    class Meta:
        ordering = ['-updated'] #정렬 기준 ,,
    def __str__(self):
        return self.author.username + " " + self.created.strftime("%Y-%m-%d %H:%M:%S")
    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=[str(self.id)])