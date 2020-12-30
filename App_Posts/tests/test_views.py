from django.test import TestCase, Client
from django.urls import reverse
from App_Posts.models import Post, Like
import json 
class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('App_Posts:home')
        self.liked_url = reverse('App_Posts:liked',args=['pk'])


    def test_home_GET(self):
    response = self.client.get(self.home_url)
    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, 'App_Posts/home.html')  

    def test_liked_GET(self):
    response = self.client.get(self.liked_url)
    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, 'App_Posts/navbar.html')      