from __future__ import unicode_literals

from django.db import models

class DateHelper(models.Model):
    """
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
