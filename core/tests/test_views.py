from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

# APIClient app
client = Client()


class GetWeatherData(TestCase):
    def setUp(self):
        self.days = 2

    def get_one_data_data(self):
        response = Client.get(reverse('get_default_data'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def get_multiple_days_data(self):
        response = Client.get(
            reverse('get_multiple_days', {'days': self.days}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
