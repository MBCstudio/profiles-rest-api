from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
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


class HelloViewsets(viewsets.ViewSet):
    """Przykładwowa klasa pokazujaca działanie Viewstes"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        a_viewset = [
            "Viewset #1",
            "Lista_1",
        ]
        return Response({'massage':'Hello!', 'a_viewset':a_viewset})

    def create(self, request):
        """Tworzenie nowego obiektu"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('imie')
            massage = f"Hello {name}!"
            return Response({'massage':massage})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Funkcja do pobierania id przedmiotu"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Funkcja updaejtuje dane"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Funkcja do updaejtowania ale tylko częsci danych"""
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk=None):
        """Funkcja do usuwania przedmiotów"""
        return Response({'http_method':'DELETE'})
