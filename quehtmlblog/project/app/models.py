from django.db import models

# Create your models here.
class Cooking(models.Model):
    cook_image=models.ImageField(upload_to='image/')
    cook_name = models.CharField(max_length=50)
    cook_email = models.EmailField()
    cook_contact = models.IntegerField()
    cook_foods = models.CharField(max_length=50)
    cook_recipes = models.CharField(max_length=50)
    cook_pass = models.IntegerField()

    def __str__(self):
        return self.cook_name


