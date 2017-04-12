from django.db import models
from django.core.urlresolvers import reverse


class Inscription(models.Model):
    nom = models.CharField(max_length=250)
    prenom = models.CharField('prénom', max_length=250)
    institution = models.CharField(max_length=250)
    fonction = models.CharField(max_length=250)
    email = models.EmailField()
    buffet = models.BooleanField()

    def __str__(self):
        return f'{self.prenom} {self.nom} - {self.fonction} ({self.institution})'

    def get_absolute_url(self):
        return reverse('inscription')
