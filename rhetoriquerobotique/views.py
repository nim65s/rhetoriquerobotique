from django.views.generic import CreateView, ListView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Inscription


class InscriptionCreateView(CreateView):
    model = Inscription
    fields = ['nom', 'prenom', 'institution', 'fonction', 'email', 'buffet']

    def form_valid(self, form):
        messages.success(self.request, 'Votre inscription a bien été prise en compte.')
        return super().form_valid(form)


class InscriptionListView(LoginRequiredMixin, ListView):
    model = Inscription

    def get_context_data(self, **kwargs):
        return super().get_context_data(inscriptions=Inscription.objects.count(),
                                        buffets=Inscription.objects.filter(buffet=True).count(), **kwargs)
