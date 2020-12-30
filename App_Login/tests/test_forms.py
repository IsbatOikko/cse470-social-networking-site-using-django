from django.test import SimpleTestCase
from App_Login.forms import CreateNewUser

class TestForms(SimpleTestCase):

    def test_createnewuser_form_valid_data(self):
        form = CreateNewUser(data={
            'email':'o@gmail.com',
            'username':'therock',
            'password1':'manu1999ucl',
            'password2':'manu1999ucl'
        })

        self.assertTrue(form.is_valid)


    def test_create_form_no_data(self):
        form = CreateNewUser(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),4)    