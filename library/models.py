from __future__ import unicode_literals

from django.db import models

from utils.models import DateHelper

class Book(DateHelper):
    """

    """

    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class BookCase(DateHelper):
    """

    """
    book_case_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=2000, blank=True)

    def __unicode__(self):
        return self.name
