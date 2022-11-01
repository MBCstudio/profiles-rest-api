from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Tworzenie imienia dla testu serializera"""
    imie = serializers.CharField(max_length=14)
