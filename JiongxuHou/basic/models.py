from django.db import models

# Create your models here.
class Navigation(models.Model):
    nav_name = models.CharField(max_length=200)

    def __str__(self):
        return self.nav_name