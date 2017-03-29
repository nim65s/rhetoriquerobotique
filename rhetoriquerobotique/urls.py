from django.conf.urls import url
from django.contrib import admin

from django.views.generic import TemplateView

from .views import InscriptionView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', InscriptionView.as_view(), name='inscription'),
    url(r'^description', TemplateView.as_view(template_name='description.html'), name='description'),
    url(r'^programme', TemplateView.as_view(template_name='programme.html'), name='programme'),
]
