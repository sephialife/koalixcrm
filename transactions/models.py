import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

from crm.models import Product
from accounting.models import Account
from transactions.const.Payment import *
from transactions.const.TransactionTypes import *

# Create your models here.


class FinancialTransactions(models.Model):
    account = models.ForeignKey(Account,verbose_name=_('Account'))
    payment_method_code = models.CharField(max_length=2,
            verbose_name= _('Payment method'),null=False,
            blank=False,choices=PAYMENT_METHOD_TYPES)

    # we can use many to many here cause the user offers products and services
    item_id = models.ForeignKey(Product,verbose_name=_('Product or Service id'))
    date = models.DateField(verbose_name=_('Date of transaction'),
           blank=False,null=False,default=str(datetime.date.today()))
    amount = models.FloatField(verbose_name=_('Amount of the transaction'),
             blank=False,null=False,default=0.00)
    description = models.CharField(verbose_name=_('Description of the transaction'),
                  blank=True,null=True,max_length=300)
                         


