from django.test import SimpleTestCase
from django.urls import reverse, resolve
from App_Login.views import sign_up, login_page, edit_profile, logout_user, profile, user, follow, unfollow

class Test_Urls(SimpleTestCase):

    def test_sign_up_url(self):
        url = reverse('App_Login:sign_up')
        self.assertEquals(resolve(url).func, sign_up)

    def test_login_url(self):
        url = reverse ('App_Login:login')
        self.assertEquals(resolve(url).func, login_page)

    def test_edit_url(self):
        url = reverse('App_Login:edit')
        self.assertEquals(resolve(url).func, edit_profile)

    def test_logout_url(self):
        url = reverse('App_Login:logout')
        self.assertEquals(resolve(url).func, logout_user)

    def test_profile_url(self):
        url = reverse('App_Login:profile')
        self.assertEquals(resolve(url).func, profile)

    def test_user_url(self):
        url = reverse('App_Login:user', args=['username'])
        self.assertEquals(resolve(url).func, user)        

    def test_follow_url(self):
        url = reverse('App_Login:follow',args=['username'])
        self.assertEquals(resolve(url).func, follow)

    def test_unfollow_url(self):
        url = reverse('App_Login:unfollow',args=['username'])
        self.assertEquals(resolve(url).func, unfollow)                    