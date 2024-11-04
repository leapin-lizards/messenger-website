from django.db import models

class Users(models.Model):
    name=models.CharField(max_length=20)
    userid=models.IntegerField(default=0)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name