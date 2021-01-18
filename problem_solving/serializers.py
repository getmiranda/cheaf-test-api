from rest_framework import serializers


def must_be_str(value):
    if not isinstance(value, str):
        raise serializers.ValidationError('Not a string')


class WordsSerializer(serializers.Serializer):
    """Serializes a list of words object"""
    words = serializers.ListField(
        child=serializers.CharField(validators=[must_be_str]), required=True
    )
