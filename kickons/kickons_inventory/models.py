from django.db import models

# Create your models here.


from django.db import models


class User(models.Model):

    f_name = models.CharField(max_length=20)
    l_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    mobile = models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=20)
    password = models.CharField(max_length=65, default='none')
    isDeliverer = models.BooleanField(default=False)

    def __str__(self):
        return self.f_name



    def getAge(self):
        return self.f_name, ' has an age of ', self.age

    def getEmail(self):
        return self.email

    def deliveryCheck(self):
        if (self.isDeliverer):
            return self

class Inventory(models.Model):
    models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=20)
    stock_count = models.CharField(max_length=20, default="calculate the count")

    def __str__(self):
        return self.item

class Item(models.Model):
    item_title = models.CharField(max_length=20)
    item_caption = models.CharField(max_length=20)
    item_price = models.CharField(max_length=4 ,default = '---')
    item_image = models.ImageField(upload_to='items')

    def __str__(self):
        return self.item_title





class DeliveryDetails(models.Model):
    on_route=models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    item_id =models.ForeignKey(Item, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_longtitude = models.FloatField(default=0)
    delivery_latitude = models.FloatField(default=0)
    deliverer = models.OneToOneField(to=Deliverer, on_delete=models.CASCADE, primary_key=True, default=0)
    #why is to_deliverer red. Fix this



    def __str__(self):
        return str(self.id)



class Deliverer(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, default=0)
    deliverer_active = models.BooleanField(default=False)
    deliverer_lat = models.FloatField(default=0)
    deliverer_long = models.FloatField(default=0)


    '''
    This will be updated when a deliverer decides to accept a job. It will show his live location. Once the delivery
    is complete, the deliverer_active will be set to False (may or may not delete the entry,  havn't decided yet)
    '''

    def __str__(self):
        return str(self.user)

class Login(models.Model):
    email = models.ForeignKey(User, on_delete=models.CASCADE, to_field='email')
    password = models.CharField(max_length=65)
    #item_image = models.CharField(max_length=20)

    def __str__(self):
        return self.email