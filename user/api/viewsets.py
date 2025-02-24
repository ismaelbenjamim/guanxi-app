from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.utils import get_instagram_username
from user.api.serializers import AccountBindSerializer
from user.models import Account


class AccountBindAPIView(APIView):
    serializer_class = AccountBindSerializer

    def post(self, request, *args, **kwargs):
        username = get_instagram_username(request.data.get('session_id'))
        print(username)
        print({**request.data, 'account': username})
        serializer = self.serializer_class(data={**request.data, 'account': username})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "success": True
        }, status=status.HTTP_200_OK)
