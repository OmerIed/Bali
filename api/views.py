from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from datetime import datetime
# Create your views here.


@api_view(['GET'])
def check_server(request):
    date = datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    message = 'server is live current time is:'
    return Response(data=message + date, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def restricted(request, *args, **kwargs):
    return Response(data='Only for logged in users', status=status.HTTP_200_OK)

