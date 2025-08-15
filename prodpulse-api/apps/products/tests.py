from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Category, Product

class ProductModelTest(APITestCase):
    def test_str_method(self):
        cat = Category.objects.create(name='TestCat', slug='test-cat')
        prod = Product.objects.create(
            title='Widget', sku='WID123', category=cat
        )
        self.assertEqual(str(prod), 'Widget (WID123)')


class ProductAPITest(APITestCase):
    def setUp(self):
        self.cat = Category.objects.create(name='TestCat', slug='test-cat')
        self.prod = Product.objects.create(
            title='Widget', sku='WID123', category=self.cat
        )

    def test_list_products(self):
        url = reverse('product-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_duplicate_sku_fails(self):
        url = reverse('product-list')
        payload = {
            'title': 'Another Widget',
            'sku': 'WID123',
            'category_id': self.cat.id
        }
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)