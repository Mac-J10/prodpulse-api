from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from products.models import Category, Product
from .models import Pulse

class PulseModelTest(APITestCase):
    def test_str_method(self):
        cat = Category.objects.create(name='TestCat', slug='test-cat')
        prod = Product.objects.create(
            title='P1', sku='P1', category=cat
        )
        pulse = Pulse.objects.create(
            product=prod,
            timestamp='2025-01-01T00:00:00Z',
            value=12.3456,
            unit='u'
        )
        self.assertIn('Pulse for P1', str(pulse))


class PulseAPITest(APITestCase):
    def setUp(self):
        cat = Category.objects.create(name='TestCat', slug='test-cat')
        self.prod = Product.objects.create(
            title='P1', sku='P1', category=cat
        )
        self.pulse = Pulse.objects.create(
            product=self.prod,
            timestamp='2025-01-01T00:00:00Z',
            value=12.3456,
            unit='u'
        )

    def test_list_pulses(self):
        url = reverse('pulse-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_pulse(self):
        url = reverse('pulse-list')
        payload = {
            'product': self.prod.id,
            'timestamp': '2025-01-01T00:00:00Z',
            'value': 12.3456,
            'unit': 'u'
        }
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_duplicate_pulse_fails(self):
        url = reverse('pulse-list')
        payload = {
            'product': self.prod.id,
            'timestamp': '2025-01-01T00:00:00Z',
            'value': 12.3456,
            'unit': 'u'
        }
        response = self.client.post(url, payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
