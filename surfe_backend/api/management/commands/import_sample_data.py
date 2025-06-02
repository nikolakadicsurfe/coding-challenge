from django.core.management.base import BaseCommand
from api.models import User, Action
import json

class Command(BaseCommand):
    help = 'Import sample data from JSON files into the database'

    def handle(self, *args, **kwargs):
        # Load users
        with open('users.json') as f:
            users_data = json.load(f)
            for user in users_data:
                User.objects.create(id=user['id'], name=user['name'], created_at=user['createdAt'])

        # Load actions
        with open('actions.json') as f:
            actions_data = json.load(f)
            for action in actions_data:
                Action.objects.create(id=action['id'], type=action['type'], user_id_id=action['userId'], target_user=action.get('targetUser'), created_at=action['createdAt'])

        self.stdout.write(self.style.SUCCESS('Sample data imported successfully')) 