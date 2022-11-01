from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAPI(APIView):
    """przykład działanie klasy APIView"""

    def get(self, request,format=None):
        """Zwraca przykładową liste API"""
        an_apiview = [
            "Coś tam wpisałem",
            "Napis nr.2",
            "Próba nr.3",
        ]

        return Response({'message':"Hello!", 'an_apiview':an_apiview})
