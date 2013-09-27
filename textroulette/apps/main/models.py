from django.db import models


class UserNumber(models.Model):
    phone_number = models.PositiveIntegerField()
    connected = models.OneToOneField('UserNumber')
