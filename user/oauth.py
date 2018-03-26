from .models import User

class OAuth(object):
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

    def authenticate(self, openid=None):
        try:
            user = User.objects.get(openid=openid)
            if user is not None:
                return user

            return None
        except User.DoesNotExist:
            return None
