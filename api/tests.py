# from django.test import TestCase

# # Create your tests here.
# def add(a, b):
#   return a+b

# class TestAddTwoValues(TestCase):
#   def test_add(self):
#     sum = add(3,5)
#     print(sum)
#     self.assertEqual(sum,8)


from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from status.models import Status
from django.contrib.auth.models import User

class StatusTest(APITestCase):
    def setUp(self):
        new_user = User(username="tanbirAhamed", password="1234")
        new_user.save()
        status = Status(text="sample test",user=new_user)
        status.save()

    def test_create_account(self):
        url = reverse('status_view')
        response = self.client.get(url,format='json')
        print(response)
        self.assertFalse(response,None)
        

