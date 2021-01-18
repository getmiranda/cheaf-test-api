from rest_framework import serializers


def must_be_str(value):
    if not isinstance(value, str):
        raise serializers.ValidationError('Not a string')


def two_coordinates(list):
    if len(list) != 2:
        raise serializers.ValidationError('must be only two coordinates')


class WordsSerializer(serializers.Serializer):
    """Serializes a list of words object"""
    words = serializers.ListField(
        child=serializers.CharField(validators=[must_be_str]), required=True
    )


class Coordinate(serializers.Serializer):
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()


class Point(serializers.Serializer):
    point1 = Coordinate(read_only=True)
    point2 = Coordinate(read_only=True)
