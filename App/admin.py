"""
    admin.py
"""

from django.contrib import admin
from .models import TransactionInformation

class TransactionInformationAdmin(admin.ModelAdmin):
    """
        This class defines an admin interface for managing transaction information with fields
        such as bank account, bank name, deposit amount, etc..
    """
    list_display = ('id', 'bank_account', 'bank_name', 'deposit_amount', 'datetime', 'status')
admin.site.register(TransactionInformation, TransactionInformationAdmin)
