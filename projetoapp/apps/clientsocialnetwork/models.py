from django.db import models
from clients.models import Client
from socialnetworks.models import Socialnetwork
# Create your models here.
class ClientSocialnetwork(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    socialnetwork = models.ForeignKey(Socialnetwork, on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Rede Social do Cliente'
        verbose_name_plural = 'Redes Sociais dos Clientes'
        ordering = ['id']

    def __str__(self):
        return f"{self.client.first_name} - {self.socialnetwork.name}"
