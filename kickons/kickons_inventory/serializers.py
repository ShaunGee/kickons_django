from rest_framework import serializers
from .models import User,Login, Item, DeliveryDetails, Deliverer
import io

'''
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('f_name', 'l_name')

'''


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'



class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class DeliveryDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryDetails
        fields = '__all__'



class DelivererSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deliverer
        fields = '__all__'


class GetDeliveryDetailsSerializer(serializers.ModelSerializer):

    class ItemDeliverySerializer(serializers.ModelSerializer):
        class Meta:
            model = Item
            fields = ['id', 'item_title', 'item_image']

    #user_id = UserSerializer()
    item_id = ItemDeliverySerializer()


    class Meta:
        model = DeliveryDetails
        fields = '__all__'

# class GetDeliveriesPerUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DeliveryDetails
#         fields = '__all__'



class GetSerializer(serializers.ModelSerializer):

    delivery_details_id = GetDeliveryDetailsSerializer()

    class Meta:
        model = Deliverer
        fields = '__all__'