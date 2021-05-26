from rest_framework import serializers
from .models import User,Login, Item
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


