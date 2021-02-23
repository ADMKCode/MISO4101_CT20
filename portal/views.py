from django.shortcuts import render
from django.http import JsonResponse
from portal.models import Deportista, Participacion
from portal.serializers import ParticipacionSerializer, DeportistaSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.


@api_view(['GET', 'POST'])
def calendario_list(request):

    if request.method == 'GET':
        calendars = Participacion.objects.all()
        serializer = ParticipacionSerializer(calendars, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ParticipacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET', 'PUT'])
def calendar_detail(request, pk):
    try:
        calendar = Participacion.objects.get(pk=pk)
    except Participacion.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = ParticipacionSerializer(calendar)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ParticipacionSerializer(calendar, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def deportista_list(request):

    if request.method == 'GET':
        deportists = Deportista.objects.all()
        serializer = DeportistaSerializer(deportists, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DeportistaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
def deportist_detail(request, pk):
    try:
        deportist = Deportista.objects.get(pk=pk)
    except Deportista.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        serializer = DeportistaSerializer(deportist)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DeportistaSerializer(deportist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def participacionView(request):
    participacion = {
        'fecha': '21-02-2021',
        'hora': '7:41',
        'deporte': 'Senderismo',
        'deportista': 'Anyelo',
        'modalidad': 'Trekkin',
        'resultado': '1er puesto'
    }

    data = Participacion.objects.all()
    response = {
        'calendario':
        list(
            data.values('fecha', 'hora', 'deporte', 'deportista', 'modalidad',
                        'resultado'))
    }

    return JsonResponse(response)


def deportistaView(request):
    data = Deportista.objects.all()
    response = {
        'deportista':
        list(
            data.values('user', 'fecha_nacimiento', 'peso', 'estatura',
                        'entrenador', 'imagen', 'lugar_nacimiento'))
    }

    return JsonResponse(response)
