from django.db import models
from django.conf import settings

class Client(models.Model):
    name = models.TextField(default = "brutaldon")
    api_base_id = models.URLField(default="https://mastodon.social")
    client_id = models.TextField(null=True, blank=True)
    client_secret = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name + ": " + self.api_base_id

class Account(models.Model):
    username = models.EmailField()
    django_user = models.ForeignKey(settings.AUTH_USER_MODEL, models.CASCADE, null=True)
    access_token = models.TextField(null=True, blank=True)
    client= models.ForeignKey(Client, models.SET_NULL, null=True)
