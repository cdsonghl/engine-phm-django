from django.db import models

class User(models.Model):
    username = models.CharField("username", max_length=30, unique=True)
    password= models.CharField("password",max_length=32)
    created_time = models.DateTimeField('create_time',auto_now_add=True)
    updated_time = models.DateTimeField('uodate_time',auto_now_add=True)

    def __str__(self):
        return "用户" + self.username