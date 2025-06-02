from django.urls import path
from . import views

urlpatterns = [
    path('user/<int:user_id>/', views.fetch_user_by_id, name='fetch_user'),
    path('user/<int:user_id>/actions/', views.get_total_actions_for_user, name='get_total_actions'),
] 