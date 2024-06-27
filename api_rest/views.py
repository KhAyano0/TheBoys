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

@api_view(['GET', 'PUT'])
def get_by_nick(request,nick):

    try:
        character = Character.objects.get(character_nickname__contains= nick)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    if request.method == 'GET':
        serializer = CharacterSerializer(character)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        serializer = CharacterSerializer(character, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

#Par URL
@api_view(['GET', 'POST','PUT', 'DELETE', ])
def character_manager(request):
    if request.method == 'GET':
        try:
            if request.GET['character']:
                character_nickname = request.GET['character']
                try:
                    character = Character.objects.get(pk=character_nickname)
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)
                serializer = CharacterSerializer(character)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)    


            

    
#Méthode post
#25/06/24 Jeff
    
    if request.method == 'POST' :
        new_character = CharacterSerializer(data=new_character)
        if serializer.is_valid():
            serializer.save
            return Response(serializer.data, status=status.HTTP_201_CREATED) #Si valide
        return Response(status=status.HTTP_400_BAD_REQUEST) #Si invalide

#PUT
    if request.method == 'PUT':
        nickname = request.data['character_nickname']
        try:

            update_character = Character.objects.get(pk=nickname)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        print(request.data)
        serializer = CharacterSerializer(update_character, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

#DELETE
    if request.method == 'DELETE':
        try:
            character_to_delete = Character.objects.get(pk=request.data[character_nickname])
            character_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
