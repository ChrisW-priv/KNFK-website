from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from KNFK_website.settings import MEDIA_ROOT


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        try:
            img = Image.open(self.image.path)
        except FileNotFoundError:
            default = MEDIA_ROOT + '/default.jpg'
            img = Image.open(default)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

