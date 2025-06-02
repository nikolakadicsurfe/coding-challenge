from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from api.models import User, Action
from django.db.models import Count, F
from collections import Counter

# Create your views here.

def fetch_user_by_id(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return JsonResponse({
        'id': user.id,
        'name': user.name,
        'created_at': user.created_at.isoformat()
    })

def get_total_actions_for_user(request, user_id):
    count = Action.objects.filter(user_id=user_id).count()
    return JsonResponse({'count': count})

def get_action_type_breakdown(request, action_type):
    actions = Action.objects.filter(type=action_type).order_by('user_id', 'created_at')
    total_actions = actions.count()
    if total_actions == 0:
        return JsonResponse({})

    next_action_types = []
    for action in actions:
        next_action = Action.objects.filter(user_id=action.user_id, created_at__gt=action.created_at).order_by('created_at').first()
        if next_action:
            next_action_types.append(next_action.type)

    breakdown = Counter(next_action_types)
    result = {action_type: count / total_actions for action_type, count in breakdown.items()}
    return JsonResponse(result)

def calculate_referral_index(request):
    referral_index = {}
    users = User.objects.all()

    for user in users:
        referred_users = set()
        stack = [user.id]

        while stack:
            current_user_id = stack.pop()
            actions = Action.objects.filter(type='REFER_USER', user_id=current_user_id)
            for action in actions:
                if action.target_user not in referred_users:
                    referred_users.add(action.target_user)
                    stack.append(action.target_user)

        referral_index[user.id] = len(referred_users)

    return JsonResponse(referral_index)
