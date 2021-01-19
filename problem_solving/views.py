from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from geopy.distance import geodesic
from geopy.geocoders import Nominatim

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
    operation_description="Return distance between these two points",
    methods=['POST'],
    request_body=serializers.Point,
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

    if 'point1' in request.data and 'point2' in request.data:
        point1 = request.data['point1']
        point2 = request.data['point2']

        try:
            distance = geodesic(point1.values(), point2.values()).kilometers
            geolocator = Nominatim(user_agent="cheaf-api")

            address_1 = geolocator.reverse(point1.values())
            address_2 = geolocator.reverse(point2.values())

            response = {
                'distance': '{:.2f} kilometers'.format(distance),
                'point1': address_1.address if address_1 else 'You are at sea',
                'point2': address_2.address if address_2 else 'You are at sea'
            }

            return Response(status=status.HTTP_200_OK, data=response)
        except Exception as error:
            print(f'EXCEPTION: {error}')
            response = {'error': str(error)}
    else:
        response = {'error': 'Invalid params'}

    return Response(status=status.HTTP_400_BAD_REQUEST, data=response)
