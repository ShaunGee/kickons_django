from django.urls import include,path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'login', views.LoginViewSet)
#router.register('r.users', views.U)


for url in router.urls:
   print(url, '\n')


urlpatterns = [
    path('', include(router.urls)),
    #path('login', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
