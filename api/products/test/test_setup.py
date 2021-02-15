# # import datetime

from authentication.models import User
from django.urls import reverse
# from faker import Faker
from rest_framework.test import APITestCase
# # # from products.models import Product

class TestSetUpProducts(APITestCase):
    def setUp(self):
        # self.products_url = reverse('products')
        # self.fake = Faker()
        
        self.login_url = reverse('login')
        
        self.user_data = { 
            'email': "test@mail.com",
            'username': "usertestcase",
            'password': "testuser",
            }

        return super().setUp()
        
    def tearDown(self): 
        return super().tearDown()
