from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, action

from .serializers import UserSerializer, LoginSerializer, ItemSerializer, DeliveryDetailsSerializer, \
    DelivererSerializer, GetDeliveryDetailsSerializer, GetSerializer
from .models import User, Login, Item, DeliveryDetails, Deliverer
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(['get', ], detail=False)
    def newest(self, request):
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

    @action(['post', ], detail=False)
    def verification(self, request):
        try:
            # incoming password and email from client
            incomingPassword = self.request.data['password']
            incomingEmail = self.request.data['email']

            # uses the incoming email to retrieve the corrosponding information in database

            user = User.objects.get(email=incomingEmail)

            dbUn = user.email
            dbPwd = user.password

            # checks to see if incoming password matches the stored username in db belonging to the user whos email matches incoming email
            if incomingPassword == dbPwd:
                print("match")
                response = {
                    'status': 'logged in',
                    'user_id': user.id,
                    'f_name': user.f_name,
                    'l_name': user.l_name,
                    'email': user.email,
                    'isDeliverer': user.isDeliverer,
                }

                return JsonResponse(response)
                # return JsonResponse({'status': 'logged in'})
        # if username doesn't exists then following execption is catcbed and 'user doesn't exist' gets sent back as a response
        except ObjectDoesNotExist:
            print('doesnt exist')
        return JsonResponse({'status': 'not logged in'})


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class DeliverViewSet(viewsets.ModelViewSet):
    queryset = DeliveryDetails.objects.all()
    serializer_class = DeliveryDetailsSerializer

    @action(['put'], detail=False)
    def update_on_route_status(self, request):
        #print("sdfsdfsdfsdfsdfsdfsdfsdfsdfsdf")
        #print(self.request.data)
        deliveryId = self.request.data['id']
        delivery = DeliveryDetails.objects.get(id=deliveryId)

        delivery.on_route = self.request.data['on_route']
        delivery.save()

        return JsonResponse({'success': 'success'})


class DelivererViewSet(viewsets.ModelViewSet):
    queryset = Deliverer.objects.all()
    serializer_class = DelivererSerializer




class GetDeliveriesViewSet(viewsets.ModelViewSet):
    queryset = DeliveryDetails.objects.filter(on_route = False)
    serializer_class = GetDeliveryDetailsSerializer




    @action(['get',], detail=True)
    def get_all_deliveries_of_user(self, request, **kwargs):

        print(self.request.data)
        pk = self.request.data[0]['user_id']
        #pk = self.request.data[0]['user_id']
        print(pk)

        deliveries = Deliverer.objects.filter(user_id=pk)
        serializer = GetSerializer(deliveries, many=True, context={'request':request})
        print(serializer.data)

        return Response(serializer.data)

'''
    @action(['put',], detail=False)
    def get_all_deliveries_of_user(self, request, **kwargs):
        pk = self.request.data[0]['user_id']
        print(pk)

        deliveries = Deliverer.objects.filter(user_id=pk)
        serializer = GetSerializer(deliveries, many=True, context={'request':request})
        print(serializer.data)

        return Response(serializer.data)
      
'''