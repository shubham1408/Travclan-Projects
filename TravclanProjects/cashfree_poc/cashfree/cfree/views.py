from rest_framework import viewsets
from rest_framework import status, views, response
from django.core import serializers
from django.http import HttpResponse
from django.conf import settings


class PaymentOrderAPI(views.APIView):
    def get(self, request):
        
        return response.Response(
            {'message': "Pyament order succesfull"},
            status=status.HTTP_200_OK
        )