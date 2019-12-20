from django.test import TestCase, Client
from django.urls import reverse
from boimelawebApp.models import Stall, Book
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('boimelaApp-home')
        self.latest_url = reverse('boimelaApp-latest')
        self.navigation_url = reverse('boimelaApp-navigation')

    def test_home_GET(self):

        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'boimelaApp/index.html')

    def test_latest_GET(self):

        response = self.client.get(self.latest_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'boimelaApp/latestbook.html')

    def test_navigation_GET(self):

        response = self.client.get(self.navigation_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'boimelaApp/navigation.html')
