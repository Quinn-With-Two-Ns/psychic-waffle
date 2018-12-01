from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)

class Restrictions(models.Model):
    type = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Food(models.Model):
    name =  models.CharField(max_length=100)


class Nutrients(models.Model):
    name = models.CharField(max_length=100)
    amount = models.IntegerField()
    user = models.ForeignKey(Food, on_delete=models.CASCADE)

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(Food, on_delete=models.CASCADE)
