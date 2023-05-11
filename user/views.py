from django.contrib.auth.models import User
from .serializer import UserSerializer
from rest_framework import viewsets
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.views import TokenObtainPairView
import jwt
from django.conf import settings
import datetime

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        return serializer.save(
            password=make_password(serializer.validated_data["password"])
        )
    
class MyTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Obtener el payload del token de acceso
        access_token_payload = serializer.validated_data.get('access')

        # Decodificar el payload del token de acceso
        decoded_token = jwt.decode(access_token_payload, algorithms=['HS256'], verify=False, key=settings.JWT_KEY)
                
        user_id = decoded_token.get('user_id')
        expirated_date = decoded_token.get('exp')
        fecha = datetime.datetime.fromtimestamp(expirated_date)
        
        response.data['user_id'] = user_id
        response.data['expirated_date'] = fecha
        
        return response