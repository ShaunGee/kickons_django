from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, action

from .serializers import UserSerializer, LoginSerializer, ItemSerializer, DeliveryDetailsSerializer, \
    DelivererSerializer, GetDeliveryDetailsSerializer, GetSerializer, GetDeliveriesPerUserSerializer
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

        deliveryId = self.request.data['id']
        #delivererID = self.request.data['deliverer_id']
        #print(delivererID)

        delivery = DeliveryDetails.objects.get(id=deliveryId)
        #deliverer = Deliverer.objects.get(user=delivererID)

        #deliverer.deliverer_active = True
        delivery.on_route = self.request.data['on_route']


        delivery.save()
        #deliverer.save()

        return JsonResponse({'success': 'success'})

'''
we want to show the delivery details of a deliverer where on_route is true and delivered is false
'''



class DelivererViewSet(viewsets.ModelViewSet):

    queryset = Deliverer.objects.all()
    serializer_class = DelivererSerializer

    @action(['post',], detail=False)
    def cancel_delivery(self, request):

        deliverer_id = self.request.data['Deliverer_id']
        delivery_details_id = self.request.data['DeliveryDetails_id']
        deliverer = Deliverer.objects.get(user=deliverer_id)
        deliverer.deliverer_active = False
        deliverer.save()

        deliveryDetails = DeliveryDetails.objects.get(id=delivery_details_id)
        deliveryDetails.delivered = False
        deliveryDetails.on_route = False
        deliveryDetails.save()

#        deliverer_model = Deliverer.objects.get(id = deliverer_id)


        return JsonResponse({'success': 'success'})

    @action(['post',], detail=False)
    def update_deliverer_active_status(self, request):
        delivererId = self.request.data['user']
        deliveryDetailId = self.request.data['DeliveryDetails']

        print('deliveryID: '+ str(delivererId))
        deliverer = Deliverer.objects.get(user=delivererId)
        deliverer.deliverer_active = True
        deliverer.DeliveryDetails = DeliveryDetails.objects.get(id=deliveryDetailId)
        deliverer.save()

        return JsonResponse({'success': 'success'})


class GetDeliveriesViewSet(viewsets.ModelViewSet):
    queryset = DeliveryDetails.objects.filter(on_route = False).filter(delivered = False)
    serializer_class = GetDeliveryDetailsSerializer


    @action(['post',], detail=False)
    def get_all_deliveries_of_user(self, request, **kwargs):

        deliverer_id = self.request.data[0]['deliverer_id']
        print(deliverer_id)
        deliverer = Deliverer.objects.filter(user = deliverer_id).filter(deliverer_active = True).filter(DeliveryDetails__delivered = False).filter(DeliveryDetails__on_route = True)
        serializer = GetDeliveriesPerUserSerializer(deliverer, many=True, context={'request':request})

        return Response(serializer.data)
