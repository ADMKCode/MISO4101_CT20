from django.shortcuts import render
from portal.models import Deportista
from portal.serializers import DeportistaSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['GET', 'POST'])
def deportista_list(request):

    if request.method == 'GET':
        deportistas = Deportista.objects.all()
        serializer = DeportistaSerializer(deportistas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DeportistaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def deportista_detail(request, pk):
    try:
        deportista = Deportista.objects.get(pk=pk)
    except Deportista.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DeportistaSerializer(deportista)
        return Response(serializer.data)

    elif request.method == 'PUT':
        DeportistaSerializer(deportista, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)