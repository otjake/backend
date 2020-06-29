from rest_framework import serializers
from .models import Customers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(many=True, queryset=Customers.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'customer']


class CustomerSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='accounts_api:customer-detail', lookup_field='pk')
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Customers
        fields = [
                'url',
                'pk',
                'owner',
                'customer_name',
                'customer_email',
                'customer_phone_number',
                'customer_acct_balance',            
        ]


