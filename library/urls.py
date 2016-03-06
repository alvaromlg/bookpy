from django.conf.urls import patterns, url, include
from rest_framework import routers

from views import BookDetail, BookList

urlpatterns = patterns(
    '',
    url(r'^books/$', BookList.as_view()),
    url(r'^books/(?P<pk>[0-9]+)/$', BookDetail.as_view()),
)
