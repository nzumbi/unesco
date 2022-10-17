#from django.db import models

# Create your models here.
from django.db import models




class Category(models.Model) :
    name = models.CharField(max_length=128,null=True)

    def __str__(self) :
        return self.name

class Iso(models.Model) :
    name = models.CharField(max_length=128,null=True)


    def __str__(self) :
        return self.name





class Region(models.Model) :
    name = models.CharField(max_length=128,null=True)
    category = models.CharField(max_length=128,null=True)
    states = models.CharField(max_length=128,null=True)
    #region = models.CharField(max_length=128,null=True)
    iso = models.CharField(max_length=128,null=True)

    def __str__(self) :
        return self.name

class State(models.Model) :
    name = models.CharField(max_length=128,null=True)
    category = models.CharField(max_length=128,null=True)
    iso = models.CharField(max_length=128,null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE,null=True)

    def __str__(self) :
        return self.name




class Site(models.Model):
    name = models.CharField(max_length=128,null=True)
    description = models.CharField(max_length=128,null=True)
    justification = models.CharField(max_length=128,null=True)
    year = models.IntegerField(null=True)
    longitude = models.CharField(max_length=128,null=True)
    latitude = models.CharField(max_length=128,null=True)
    area_hectares = models.CharField(max_length=128,null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    states = models.ForeignKey(State, on_delete=models.CASCADE,null=True)
    region = models.CharField(max_length=128,null=True)
    iso = models.ForeignKey(Iso, on_delete=models.CASCADE,null=True)




    def __str__(self) :
        return self.name






