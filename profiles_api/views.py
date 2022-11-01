from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


class HelloAPI(APIView):
    """przykład działanie klasy APIView"""
    serializer_class = serializers.HelloSerializer

    def get(self, request,format=None):
        """Zwraca przykładową liste API"""
        an_apiview = [
            "Coś tam wpisałem",
            "Napis nr.2",
            "Próba nr.3",
        ]

        return Response({'message':"Hello!", 'an_apiview':an_apiview})

    def post(self, request):
        """tworzenie wiadomosci pocztkowej z imieniem"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('imie')
            massage = f"Hello {name}"
            return Response({'massage': massage})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """do updatów objektow"""
        return Response({'method':'PUT'})

    def path(self, request, pk=None):
        """do robienia updatów objektow ale czesciowych"""
        return Response({'method':'PATH'})

    def delete(self, request, pk=None):
        """do usuwania odjektow"""
        return Response({'method': 'DELETE'})
