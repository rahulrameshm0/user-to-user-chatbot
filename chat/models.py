from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=100, unique=True, null=False)
    email = models.EmailField(max_length=100, unique=True, null=False)
    password = models.CharField(max_length=100, null=False)
    confirm_password = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.username
    
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} ➡️ {self.receiver}: {self.message[:20]}"
