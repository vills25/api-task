from django.db import models

# Create your models here.
class task(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, unique = True)
    password = models.CharField(max_length = 255, blank = True)

    def __str__(self):
        return self.email, self.name, self.password
