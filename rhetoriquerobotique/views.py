from django.views.generic import CreateView
from django.contrib import messages

from .models import Inscription


class InscriptionView(CreateView):
    model = Inscription
    fields = ['nom', 'prenom', 'institution', 'fonction', 'email', 'buffet']

    def form_valid(self, form):
        messages.success(self.request, 'Votre inscription a bien été prise en compte.')
        return super().form_valid(form)
