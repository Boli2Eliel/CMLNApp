from django.db import models
from django.contrib.auth.models import User
from cmlnGestion.models.model_membre import Extension


# Create your models here.
class Profile(models.Model):
    #staff = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    extension = models.ForeignKey(Extension, on_delete= models.CASCADE, null=True, blank=True, verbose_name="Extension")
    address = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=20, null=True)
    image = models.ImageField(default='avatar.jpg', upload_to='Profile_Images', null=True)
    job_function = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.staff.username}-Profile'