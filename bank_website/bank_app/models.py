from django.db import models

# Create your models here.
class Banking(models.Model):
    head_name=models.CharField(max_length=250)
    desc=models.TextField()

    img=models.ImageField(upload_to='Images')

    def __str__(self):
        return self.head_name