"""
    models.py
"""

from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime

class TransactionInformation(models.Model):
    """
        A model representing transaction information.
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20)
    national_code = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    deposit_amount = models.CharField(max_length=100)
    bank_account = models.CharField(max_length=30)
    bank_name = models.CharField(max_length=100)
    datetime = models.DateTimeField(default=datetime.now(), editable=False)
    status = models.CharField(max_length=30, default="None", editable=False)

    class Meta:
        """
            This class represents the metadata for the transaction_information model.
        """
        verbose_name = _("Transaction Information")
        verbose_name_plural = _("Transaction Information")

    def __str__(self):
        return str(self.bank_account)
