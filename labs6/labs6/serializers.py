from rest_framework import serializers
from .models import Agent,Property,Client,Request

class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['id','first_name','last_name','specialty']

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['id', 'type', 'address', 'price', 'agent']

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'contact_email']

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['id', 'client', 'property']