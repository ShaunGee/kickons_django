
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, action

from .serializers import UserSerializer, LoginSerializer, ItemSerializer, DeliveryDetailsSerializer, DelivererSerializer, GetDeliveryDetailsSerializer
from .models import User,Login, Item, DeliveryDetails, Deliverer
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
    queryset = User.objects.all()
    serializer_class = UserSerializer


    @action(['post',], detail=False)
    def verification(self,request):
        try:
            #incoming password and email from client
            incomingPassword = self.request.data['password']
            incomingEmail = self.request.data['email']

            #uses the incoming email to retrieve the corrosponding information in database

            user = User.objects.get(email=incomingEmail)

            dbUn = user.email
            dbPwd = user.password

            #checks to see if incoming password matches the stored username in db belonging to the user whos email matches incoming email
            if incomingPassword == dbPwd:
                print("match")
                response = {
                    'status':'logged in',
                    'user_id': user.id,
                    'f_name': user.f_name,
                    'l_name': user.l_name,
                    'email': user.email,
                }


                return JsonResponse(response)
                #return JsonResponse({'status': 'logged in'})
        #if username doesn't exists then following execption is catcbed and 'user doesn't exist' gets sent back as a response
        except ObjectDoesNotExist:
            print('doesnt exist')
        return JsonResponse({'status': 'not logged in'})


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer



class DeliverViewSet(viewsets.ModelViewSet):

    #queryset below filter only gets data where on_route = false to be sent
    queryset = DeliveryDetails.objects.all().filter(on_route = False)
    serializer_class = DeliveryDetailsSerializer


    def list(self, request, *args, **kwargs):


        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        print('retrieve')
        return super().retrieve(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        print('create')
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        print('update')
        return super().update(request, *args, **kwargs)

class DelivererViewSet(viewsets.ModelViewSet):
    queryset = DeliveryDetails.objects.all()
    serializer_class = DelivererSerializer

class GetDeliveriesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DeliveryDetails.objects.filter(on_route=False)
    serializer_class = GetDeliveryDetailsSerializer