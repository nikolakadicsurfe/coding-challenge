from django.test import TestCase
from django.urls import reverse
from api.models import User, Action
from django.utils.dateparse import parse_datetime

class UserAPITests(TestCase):
    def setUp(self):
        # Create sample users
        User.objects.create(id=1, name='John Doe', created_at=parse_datetime('2022-04-14T11:12:22.758Z'))
        User.objects.create(id=2, name='Jane Smith', created_at=parse_datetime('2022-05-14T11:12:22.758Z'))

    def test_fetch_user_by_id(self):
        response = self.client.get(reverse('fetch_user', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'id': 1,
            'name': 'John Doe',
            'created_at': '2022-04-14T11:12:22.758000+00:00'
        })

    # Additional tests for other endpoints will be added here
