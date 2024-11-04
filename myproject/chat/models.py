from django.db import models
from django.contrib.auth.models import User

class Chat(models.Model):
    body=models.TextField()
    date=models.DateField(auto_now_add=True)
    #author=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
    room_name=models.CharField(max_length=15)
    def __str__(self):
        return self.body
