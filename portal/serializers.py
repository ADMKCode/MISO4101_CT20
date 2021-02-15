from rest_framework import serializers
from portal.models import Deportista


class DeportistaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deportista
        fields = ('__all__')
        #fields = ['id', 'imagen', 'peso', 'estatura']
