from django.contrib.auth.models import User
from django.db import models
# Create your models here.




class Food_Type(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class Food(models.Model):
    name = models.CharField(max_length=255)
    food_type = models.ForeignKey(Food_Type, on_delete=models.CASCADE)
    tarkibi = models.CharField(max_length=255)
    narxi = models.IntegerField()

    def __str__(self):
        return self.name



class Comment(models.Model):
    text = models.CharField(max_length=155)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.text
