from django.test import SimpleTestCase
from App_Posts.forms import PostForm

class TestForms(SimpleTestCase):

    def test_PostForm_valid_data(self):
             form = PostForm(data={
            'image':'',
            'caption':'This is It',
        })

        self.assertTrue(form.is_valid)

    def test_create_form_no_data(self):
           form = PostForm(data={})

           self.assertFalse(form.is_valid())
           self.assertEquals(len(form.errors),4)    
        
