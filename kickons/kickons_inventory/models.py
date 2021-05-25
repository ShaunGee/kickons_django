from django.db import models

# Create your models here.


from django.db import models


class User(models.Model):
    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    email = models.EmailField()
    mobile = models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    password = models.CharField(max_length=65, default='none')

    def __str__(self):
        return self.f_name

    def getAge(self):
        return self.f_name, ' has an age of ', self.age



class Inventory(models.Model):
    item = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    stock_count = models.CharField(max_length=20)

    def __str__(self):
        return self.item


class Item(models.Model):
    item = models.CharField(max_length=20)
    item_description = models.CharField(max_length=20)
    item_image = models.CharField(max_length=20)

    def __str__(self):
        return self.item


class Login(models.Model):
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=65)
    #item_image = models.CharField(max_length=20)

    def __str__(self):
        return self.email

