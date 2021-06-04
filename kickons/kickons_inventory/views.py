
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, action

from .serializers import UserSerializer, LoginSerializer, ItemSerializer, DeliverySerializer
from .models import User,Login, Item, Delivery
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse




class UserViewSet(viewsets.ModelViewSet):


    queryset = User.objects.all()
    serializer_class = UserSerializer


    @action(['get',], detail=False)
    def newest(self,request):
        newest = self.get_queryset().order_by('f_name').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)

'''
    @action(['post',], detail=False)
    def login(self, request):
        login = self.get_queryset().order_by('f_name').first()
        print(login.password)
        serializer = self.get_serializer_class()(login)
        return Response(serializer.data)
'''



class LoginViewSet(viewsets.ModelViewSet):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer


    @action(['post',], detail=False)
    def verification(self,request):
        try:
            incomingPassword = self.request.data['password']
            incomingEmail = self.request.data['email']

            print(incomingPassword)
            print(incomingEmail)

            dbUn = Login.objects.get(email=incomingEmail).email
            dbPwd = Login.objects.get(email=incomingEmail).password

            if incomingPassword == dbPwd:
                print("match")
                return JsonResponse({'status': 'logged in'})

        except ObjectDoesNotExist:
            print('doesnt exist')
        return JsonResponse({'status': 'not logged in'})


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

'''
    @action(['get',])
    def allItems(self,request):
    
        '''


class DeliverViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all();
    serializer_class = DeliverySerializer