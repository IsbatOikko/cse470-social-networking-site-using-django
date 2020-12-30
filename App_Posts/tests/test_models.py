from django.test import TestCase
from App_Posts.models import Post, Like

class TestModels(TestCase):

    def setUp(self):
    self.user1 = Post.objects.cretae(
        author = user,
        image = 'cr7.jpg',
       caption = 'this is it'
        )

    def test_user_is_assigned_slug_on_creation(self):
    self.assertEquals(self.user1.slug, 'user1')    