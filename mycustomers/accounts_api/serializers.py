from rest_framework import serializers
from .models import Customers
from django.contrib.auth.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    customer = serializers.HyperlinkedRelatedField(many=True, view_name='customer-detail', read_only=True)
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'password', 'customer']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class CustomerSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='customer-detail', lookup_field='pk')
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
