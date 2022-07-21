from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """Test API view
    """

    def get(self, request, format=None):
        """
        Returns list of APIView features
        """
        an_apiview = [
            'Uses HTTP methods as functions (get, post, delete, update)',
            'It is similar to traditional django view',
            'Gives you most control over application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
