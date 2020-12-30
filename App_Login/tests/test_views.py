from django.test import TestCase, Client
from django.urls import reverse
from App_Login.models import UserProfile, Follow
import json

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('App_Login:sign_up')
        self.login_url = reverse('App_Login:login')
        self.profile_url = reverse('App_Login:profile')
        self.user_url = reverse('App_Login:user', args=['username'])
        

    def test_signup_GET(self):
        response = self.client.get(self.signup_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'App_Login/signup.html')

    def test_login_GET(self):
        response = self.client.get(self.login_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'App_Login/login.html')

    def test_profile_GET(self):
        response = self.client.get(self.profile_url)
        self.assertEquals(response.status_code, 302)
        self.assertTemplateUsed(response, 'App_Login/user.html') 


    def test_User_GET(self):
        response = self.client.get(self.user_url)
        self.assertEquals(response.status_code, 302)
        self.assertTemplateUsed(response, 'App_Login/user_other.html')    
    
    def test_Follow_GET(self):
        response = self.client.get(self.user_url)
        self.assertEquals(response.status_code, 302)
        self.assertTemplateUsed(response, 'App_Login/user.html')    

             




        
   