from rest_framework import serializers

from users import models


class UserSerializer(serializers.ModelSerializer):
    """Serializes a user object"""

    class Meta:
        model = models.User
        fields = ('id', 'email', 'password',) + tuple(models.User.REQUIRED_FIELDS)
        read_only_fields = ('id',)
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }
