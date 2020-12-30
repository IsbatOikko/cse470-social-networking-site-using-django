from django.test import TestCase
from App_Login.models import UserProfile,Follow


class TestModels(TestCase):

    def setUp(self):
        self.user1 = UserProfile.objects.create(
        user='therock',
            #user_id = 1,
            description='bring it',
            full_name='D J'
        
        )

    def test_user_is_assigned_slug_on_creation(self):
        self.assertEquals(self.user1.slug, 'user1')


     class UserProfile(models.model):       