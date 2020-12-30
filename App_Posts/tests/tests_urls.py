from django.test import SimpleTestCase
from django.urls import reverse, resolve
from App_Posts.views import home, liked, unliked

class Test_Urls(SimpleTestCase):

    def test_home_url(self):
        url = reverse('App_Posts:home')
        self.assertEquals(resolve(url).func, home)

    def test_liked_url(self):
        url = reverse('App_Posts:liked',args=['pk'])
        self.assertEquals(resolve(url).func, liked)

    def test_unliked_url(self):
        url = reverse('App_Posts:unliked',args=['pk'])
        self.assertEquals(resolve(url).func,unliked)    