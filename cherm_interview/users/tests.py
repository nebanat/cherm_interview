from django.test import TestCase
from rest_framework.test import APIClient

from .models import CustomUser


# Create your tests here.
class TestUserRegistration(TestCase):
    def setUp(self):
        self.client = APIClient()
        test_user = CustomUser(email='testuserone@gmail.com', password='somepasswordtest')
        test_user.save()

    def test_user_register_with_no_data_fails(self):
        response = self.client.post('/users/register', format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.get('email')[0], 'This field is required.')
        self.assertEqual(response.data.get('password1')[0], 'This field is required.')
        self.assertEqual(response.data.get('password2')[0], 'This field is required.')

    def test_user_registration_with_no_matching_passwords_fails(self):
        json_data = {
            'email': 'testuseremail@gmail.com',
            'password1': 'somepassword',
            'password2': 'somepassword2'
        }
        response = self.client.post('/users/register', json_data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.get('non_field_errors')[0], 'The two password fields didn\'t match.')

    def test_user_registration_with_invalid_email_fails(self):
        json_data = {
            'email': 'testuseremail',
            'password1': 'somepassword1',
            'password2': 'somepassword1'
        }

        response = self.client.post('/users/register', json_data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.get('email')[0], 'Enter a valid email address.')

    def test_user_registration_with_email_already_exists_fails(self):
        pass


class TestUserLogin(TestCase):
    def setUp(self):
        self.client = APIClient()
        test_user = CustomUser(email='testuserone@gmail.com', password='somepasswordtest')
        test_user.save()

    def test_user_login_with_no_data_fails(self):
        response = self.client.post('/users/login', format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.get('email')[0], 'This field is required.')
        self.assertEqual(response.data.get('password')[0], 'This field is required.')

    def test_user_login_with_invalid_credentials_fails(self):
        json_data = {
            'email': 'testuseremail@gmail.com',
            'password': 'somepassword',
        }

        response = self.client.post('/users/login', json_data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data.get('non_field_errors')[0], 'Account with this email/username does not exists')

    def test_user_login_with_valid_credentials_succeeds(self):
        pass

