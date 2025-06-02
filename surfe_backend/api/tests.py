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

class ActionAPITests(TestCase):
    def setUp(self):
        # Create sample users
        user1 = User.objects.create(id=1, name='John Doe', created_at=parse_datetime('2022-04-14T11:12:22.758Z'))
        user2 = User.objects.create(id=2, name='Jane Smith', created_at=parse_datetime('2022-05-14T11:12:22.758Z'))

        # Create sample actions
        Action.objects.create(id=1, type='LOGIN', user_id=user1, created_at=parse_datetime('2022-04-14T12:00:00.000Z'))
        Action.objects.create(id=2, type='LOGOUT', user_id=user1, created_at=parse_datetime('2022-04-14T13:00:00.000Z'))
        Action.objects.create(id=3, type='LOGIN', user_id=user2, created_at=parse_datetime('2022-05-14T12:00:00.000Z'))

    def test_get_total_actions_for_user(self):
        response = self.client.get(reverse('get_total_actions', args=[1]))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'count': 2
        })

class ActionTypeBreakdownTests(TestCase):
    def setUp(self):
        # Create sample users
        user1 = User.objects.create(id=1, name='John Doe', created_at=parse_datetime('2022-04-14T11:12:22.758Z'))
        user2 = User.objects.create(id=2, name='Jane Smith', created_at=parse_datetime('2022-05-14T11:12:22.758Z'))

        # Create sample actions
        Action.objects.create(id=1, type='LOGIN', user_id=user1, created_at=parse_datetime('2022-04-14T12:00:00.000Z'))
        Action.objects.create(id=2, type='LOGOUT', user_id=user1, created_at=parse_datetime('2022-04-14T13:00:00.000Z'))
        Action.objects.create(id=3, type='LOGIN', user_id=user2, created_at=parse_datetime('2022-04-14T14:00:00.000Z'))
        Action.objects.create(id=4, type='LOGIN', user_id=user2, created_at=parse_datetime('2022-04-14T15:00:00.000Z'))
        Action.objects.create(id=5, type='LOGOUT', user_id=user1, created_at=parse_datetime('2022-04-14T16:00:00.000Z'))
        Action.objects.create(id=6, type='LOGIN', user_id=user1, created_at=parse_datetime('2022-04-14T17:00:00.000Z'))
        Action.objects.create(id=7, type='LOGOUT', user_id=user1, created_at=parse_datetime('2022-04-14T18:00:00.000Z'))
        Action.objects.create(id=8, type='LOGIN', user_id=user1, created_at=parse_datetime('2022-04-14T19:00:00.000Z'))
        Action.objects.create(id=9, type='LOGOUT', user_id=user1, created_at=parse_datetime('2022-04-14T20:00:00.000Z'))
        Action.objects.create(id=10, type='LOGIN', user_id=user1, created_at=parse_datetime('2022-04-14T21:00:00.000Z'))
        Action.objects.create(id=11, type='LOGOUT', user_id=user1, created_at=parse_datetime('2022-04-14T22:00:00.000Z'))
        Action.objects.create(id=12, type='LOGIN', user_id=user2, created_at=parse_datetime('2022-04-14T23:00:00.000Z'))
        Action.objects.create(id=13, type='LOGIN', user_id=user2, created_at=parse_datetime('2022-04-15T00:00:00.000Z'))
    def test_get_action_type_breakdown(self):
        response = self.client.get(reverse('get_action_type_breakdown', args=['LOGIN']))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'LOGOUT': 0.5,
            'LOGIN': 0.5
        })

class ReferralIndexTests(TestCase):
    def setUp(self):
        # Create sample users
        user1 = User.objects.create(id=1, name='John Doe', created_at=parse_datetime('2022-04-14T11:12:22.758Z'))
        user2 = User.objects.create(id=2, name='Jane Smith', created_at=parse_datetime('2022-05-14T11:12:22.758Z'))
        user3 = User.objects.create(id=3, name='Alice Johnson', created_at=parse_datetime('2022-06-14T11:12:22.758Z'))

        # Create sample actions
        Action.objects.create(id=1, type='REFER_USER', user_id=user1, target_user=user2.id, created_at=parse_datetime('2022-04-14T12:00:00.000Z'))
        Action.objects.create(id=2, type='REFER_USER', user_id=user2, target_user=user3.id, created_at=parse_datetime('2022-05-14T13:00:00.000Z'))

    def test_calculate_referral_index(self):
        response = self.client.get(reverse('calculate_referral_index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            '1': 2,  # User 1 referred User 2 and indirectly User 3
            '2': 1,  # User 2 referred User 3
            '3': 0   # User 3 referred no one
        })
