from rest_framework import serializers
from .models import Juego


class JuegoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juego
        fields = "__all__"
        read_only_fields = ["id", "creado_en"]

    def validate_titulo(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("El título no puede estar vacío.")
        return value
