from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from problem_solving import serializers


@swagger_auto_schema(
    operation_description="Receives words and counts repetitions",
    methods=['POST'],
    request_body=serializers.WordsSerializer,
    responses={
        200: 'words counted'
    }
)
@api_view(['POST'])
def count_words(request):
    """
    Receives words and counts repetitions

    Receives 10 words at random (can be repeated) and returns a list of words
    and the number of times they appear in the list.
    """
    if 'words' in request.data:
        if isinstance(request.data['words'], list):
            count = {}

            for word in request.data['words']:
                if isinstance(word, str):
                    count[word] = count.get(word, 0) + 1
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_200_OK, data=count)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    operation_description="Receives words and counts repetitions",
    methods=['POST'],
    responses={
        200: 'Success',
        400: 'Error'
    }
)
@api_view(['POST'])
def distance_two_points(request):
    """
    Return distance between these two points

    Receives 2 Lat-Long geo-coordinates and returns the distance
    between these two points.
    """
    return Response(status=status.HTTP_200_OK)
