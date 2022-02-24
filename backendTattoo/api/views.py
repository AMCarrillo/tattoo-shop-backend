from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.core.mail import send_mail

from .models import ContactModel
from .serializers import ContactSerializer


@api_view(['POST',])
def api_create_contact_view(request):
    if request.method == "POST":
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data['name']
            email = serializer.data['email']
            message = serializer.data['message']

            # send mail
            send_mail("Message received from the website.","User {} with email {} says:\n\n {}".format(name,email,message), "", ["kenyiheral@gmail.com"], fail_silently=False)
           
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("Error")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
