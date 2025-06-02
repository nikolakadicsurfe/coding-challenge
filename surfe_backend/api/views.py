from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from api.models import User

# Create your views here.

def fetch_user_by_id(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return JsonResponse({
        'id': user.id,
        'name': user.name,
        'created_at': user.created_at.isoformat()
    })
