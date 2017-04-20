from django.conf.urls import url, include
from django.contrib import admin

from django.views.generic import TemplateView, RedirectView, ListView

from .views import InscriptionCreateView, InscriptionListView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(pattern_name='inscription', permanent=True), name='home'),
    url(r'^inscription$', InscriptionCreateView.as_view(), name='inscription'),
    url(r'^presentation', TemplateView.as_view(template_name='presentation.html'), name='presentation'),
    url(r'^programme', TemplateView.as_view(template_name='programme.html'), name='programme'),
    url(r'^liste', InscriptionListView.as_view(), name='liste'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]
