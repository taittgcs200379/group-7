from django.db import models
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name



class Store(models.Model):
    name=models.CharField(max_length=20)
    image = models.TextField()
    description = models.TextField()
    code = models.CharField(max_length=20)
    date = models.DateField()
    price= models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f" {self.name},{self.image}, {self.description}, {self.code},   {self.price}, {self.category}"
    



  