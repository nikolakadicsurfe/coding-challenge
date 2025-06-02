from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(db_index=True)

class Action(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)
    target_user = models.IntegerField(null=True, blank=True, db_index=True)
    created_at = models.DateTimeField(db_index=True)
