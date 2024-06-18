from django.db import models

class Member(models.Model):
    class Meta:
        db_table ='members'
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

