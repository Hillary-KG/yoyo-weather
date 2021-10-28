import requests
import statistics


from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from yoyo_weather import settings
from rest_framework.exceptions import APIException


@api_view(['GET'])
def home(request):
    return Response({'msg': "I am home"}, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_tempertaure(request, city, days=1):
    """
    this function contains logic for getting temperature data for given city, computing max, minimum, average,
    median and returns result:
    Expected output:
                    {
                        “maximum”: value,
                        “minimum”: value,
                        “average”: value,
                        “median”: value,   
                    }
    """
    paylaod = {
        'key': settings.API_KEY,
        'q': city,
        'days': days
    }
    temps_list = []  # initializing empty list to hold the temp data from API
    url = settings.API_URL
    if not city:
        return Response({'message': "No city submitted, city must not be empty"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        res = requests.get(url, params=paylaod)

        res_data = res.json()
        if len(res_data['forecast']['forecastday']) <= 0:
            return Response({'msg': "no data fetched"}, status=status.HTTP_200_OK)

        for day in res_data['forecast']['forecastday']:
            temps_list += [day['day']['avgtemp_c'],
                           day['day']['maxtemp_c'],
                           day['day']['mintemp_c']]

        max_temp, min_temp, avg_temp, median_temp = max(temps_list), min(
            temps_list), round(statistics.mean(temps_list), 2), statistics.median(temps_list)

        response = {'maximum': max_temp,
                    'minimum': min_temp,
                    'average': avg_temp,
                    'median': median_temp,
                    }
        return Response(response, status=status.HTTP_200_OK)
    except APIException as e:
        return Response({'message': e.detail}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
