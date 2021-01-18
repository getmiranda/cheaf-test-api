from rest_framework import viewsets

from users import models
from users import serializers


class UserViewSet(viewsets.ModelViewSet):
    """
    retrieve:
    Return the given user.

    list:
    Return a list of all the existing users.

    create:
    Create a new user instance.

    partial_update:
    Partially upgrade the given user.

    update:
    Update the given user.

    destroy:
    Delete the given user.
    """
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()
