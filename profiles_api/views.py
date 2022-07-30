from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    def get(self, request, format=None):
        an_apiview = [
            'usamos metodos http como funciones (get, post, put, patch, delete)',
            'es similar a una vista tradicional de django',
            'nos da el mayor control sobre la logica de nuestra aplicacion',
            'esta mapeado manualmente a los urls'
        ]

        return Response({'message': 'hello', 'an_apiview': an_apiview})