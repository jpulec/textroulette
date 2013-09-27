from django.db import models


class UserNumber(models.Model):
    phone_number = models.CharField(max_length=10)
    connected = models.ForeignKey('UserNumber', null=True)

    def __unicode__(self):
        return "#" + self.phone_number

class Message(models.Model):
    id = models.CharField(max_length=34, primary_key=True)
