from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^/import/$', views.ImportProcessView.as_view(), name='import_process'),
]
