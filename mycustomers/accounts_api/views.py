from django.shortcuts import render
from rest_framework import generics
from .models import Customers
from django.http import Http404
from .serializers import UserSerializer, CustomerSerializer
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from rest_framework import renderers
#from .permissions import IsOwnerOrReadOnly
#from rest_framework.authentication import SessionAuthentication, TokenAuthentication
#from rest_framework.authtoken.models import Token


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CustomerList(generics.ListCreateAPIView):
    """
    List all entered companies, or create a new customer.
    """
    queryset = Customers.objects.all()
    serializer_class = CustomerSerializer
   # authentication_classes = [TokenAuthentication, SessionAuthentication]
   # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a customer.
    """
    queryset = Customers.objects.all()
    serializer_class = CustomerSerializer
   # authentication_classes = [TokenAuthentication, SessionAuthentication]
   # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class CustomerHighlight(generics.GenericAPIView):
    '''
    Highlighting each Customer
    '''
    queryset = Customers.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        customers = self.get_object()
        return Response(customers.highlighted)

@api_view(['GET'])
def api_root(request, format=None):
    '''
    Providing endpoints for each customer
    '''
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'customers': reverse('customer-list', request=request, format=format)
    })