from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Character
from .serializers import CharacterSerializer

import json
# Create your views here.
@api_view(['GET'])
def get_characters(request):
    if request.method == 'GET':
        characters = Character.objects.all()

        serializer = CharacterSerializer(characters, many=True)

        return Response(serializer.data)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_by_nick(request,nick):

    try:
        character = Character.objects.get(character_nickname = nick)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = CharacterSerializer(character)
        return Response(serializer.data)