from itertools import product
from rest_framework import serializers

from django.contrib.auth.models import User
from .models import Store


# # Serializers define the API representation.

class StoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = '__all__'

# using without model
# class YourSerializer(serializers.Serializer):

#   place your fields here e.g 
#   store_id = serializers..CharField(max_length=32) ...and so on
