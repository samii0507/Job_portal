from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

Model = get_user_model()

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = Model.objects.get(Q(username__iexact=username) | Q(email__iexact=username))  
        except Model.DoesNotExist:
            Model().set_password(password)
            return
        except Model.MultipleObjectsReturned:
            user = Model.objects.filter(Q(username__iexact=username) | Q(email__iexact=username)).order_by('id').first()
        if user.check_password(password) and self.user_can_authenticate(user):
            return user