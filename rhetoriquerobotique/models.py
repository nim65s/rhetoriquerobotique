from django.db import models
from django.core.urlresolvers import reverse


class Inscription(models.Model):
    nom = models.CharField(max_length=250)
    prenom = models.CharField('prénom', max_length=250)
    institution = models.CharField(max_length=250)
    fonction = models.CharField(max_length=250)
    email = models.EmailField()
    buffet = models.BooleanField()

    def get_absolute_url(self):
        return reverse('inscription')
