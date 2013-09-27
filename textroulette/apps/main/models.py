from django.db import models


class UserNumber(models.Model):
    phone_number = models.CharField(max_length=10)
