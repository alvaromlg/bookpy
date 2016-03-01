from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.finder_index, name='finder'),
    url(r'^results$', views.finder_results, name='results'),
]
