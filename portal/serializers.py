from rest_framework import serializers
from portal.models import Participacion, Deportista


class ParticipacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participacion
        fields = [
            'fecha', 'hora', 'deporte', 'deportista', 'modalidad', 'resultado'
        ]


class DeportistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deportista
        fields = [
            'user', 'fecha_nacimiento', 'peso', 'estatura', 'entrenador',
            'imagen', 'lugar_nacimiento'
        ]
