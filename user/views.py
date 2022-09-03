from .serializers import UserSerializer
from .models import User
from rest_framework.views import APIView
from rest_framework.response import Response
import jwt, datetime
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed



# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

def auth_jwt(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow()
        }

    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

    response = Response()       
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
    'jwt': token,
            }
    return response

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        user = User.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        return auth_jwt(user.id)