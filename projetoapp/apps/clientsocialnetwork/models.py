from django.db import models
from clients.models import Client
from socialnetworks.models import SocialNetwork
# Create your models here.
class ClientSocialnetwork(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='socialnetworlk_client')
    socialnetwork = models.ForeignKey(SocialNetwork, on_delete=models.CASCADE, related_name='social_client_socialnetwork')
    class Meta:
        verbose_name = 'Rede Social do Cliente'
        verbose_name_plural = 'Redes Sociais dos Clientes'
        ordering = ['id']

    def __str__(self):
        return f"{self.client.first_name} - {self.socialnetwork.name}"
