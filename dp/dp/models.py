from django.contrib.postgres.fields import JSONField
from django.db import models


class UserModel(models.Model):

    data = JSONField()

    def __str__(self):
       return self.data