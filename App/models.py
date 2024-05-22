"""
    models.py
"""

from django.db import models
from django.utils.translation import gettext_lazy as _

class TransactionInformation(models.Model):
    """
        A model representing transaction information.
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    national_code = models.CharField(max_length=10)
    deposit_amount = models.DecimalField(max_digits=10, decimal_places=2)
    bank_account = models.CharField(max_length=30)
    bank_name = models.CharField(max_length=30)
    datetime = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15)

    class Meta:
        """
            This class represents the metadata for the transaction_information model.
        """
        verbose_name = _("Transaction Information")
        verbose_name_plural = _("Transaction Information")

    def __str__(self):
        return str(self.bank_account)
