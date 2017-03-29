from django.conf.urls import url
from django.contrib import admin

from django.views.generic import TemplateView, RedirectView

from .views import InscriptionView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(pattern_name='inscription', permanent=True), name='home'),
    url(r'^inscription$', InscriptionView.as_view(), name='inscription'),
    url(r'^presentation', TemplateView.as_view(template_name='presentation.html'), name='presentation'),
    url(r'^programme', TemplateView.as_view(template_name='programme.html'), name='programme'),
]
