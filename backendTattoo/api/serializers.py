from rest_framework import serializers
from .models import ContactModel

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = ['name', 'email', 'message']
  #  name = serializers.CharField()
 #   email = serializers.EmailField()
#    message = serializers.CharField()
