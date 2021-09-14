from rest_framework import status
from rest_framework.test import APITestCase

class TestApiMethods(APITestCase):
    def test_ifsc_search(self):
        response = self.client.get('/ifsc_search/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_bank_leader_board(self):
        response = self.client.get('/bank_leader_board/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_statistics(self):
        response = self.client.get('/statistics/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_count(self):
        response = self.client.get('/api_count/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_ifsc_count(self):
        response = self.client.get('/ifsc_count/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)