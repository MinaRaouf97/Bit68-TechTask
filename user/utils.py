from rest_framework.exceptions import AuthenticationFailed
from django.conf import settings
import jwt
from .models import User

def get_user(request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:    
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        except:
            raise AuthenticationFailed('Unauthenticated!')
        user = User.objects.filter(id=payload['user_id']).first()
        return user 