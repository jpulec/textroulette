from django.db import models


class UserNumber(models.Model):
    phone_number = models.CharField(max_length=10)
    connected = models.OneToOneField('UserNumber', null=True)

    def __unicode__(self):
        return "#" + self.phone_number + ":" + str(self.connected)
