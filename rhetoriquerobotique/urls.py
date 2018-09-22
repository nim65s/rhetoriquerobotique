from django.urls import path, include
from django.contrib import admin

from django.views.generic import TemplateView, RedirectView, ListView

from .views import InscriptionCreateView, InscriptionListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(pattern_name='inscription', permanent=True), name='home'),
    path('inscription', InscriptionCreateView.as_view(), name='inscription'),
    path('presentation', TemplateView.as_view(template_name='presentation.html'), name='presentation'),
    path('programme', TemplateView.as_view(template_name='programme.html'), name='programme'),
    path('liste', InscriptionListView.as_view(), name='liste'),
    path('accounts/', include('django.contrib.auth.urls')),
]
