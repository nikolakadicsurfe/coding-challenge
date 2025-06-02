from django.urls import path
from . import views

urlpatterns = [
    path('user/<int:user_id>/', views.fetch_user_by_id, name='fetch_user'),
] 