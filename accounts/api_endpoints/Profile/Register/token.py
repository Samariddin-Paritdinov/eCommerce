import jwt
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


class EmailTokenCheck:
    def __call__(self, token):
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user = User.objects.get(id=payload["user_id"])
            if not user.is_active:
                user.is_active = True
                user.save()
            return user
        except jwt.ExpiredSignatureError:
            return None
        except jwt.exceptions.DecodeError:
            return None