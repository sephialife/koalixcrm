from django.db import models 
from django.utils.translation import ugettext_lazy as _
from braces.views import PermissionRequiredMixin, LoginRequiredMixin
from crm.models import Product
from accounting.models import Account 
import datetime
# Create your models here.

class Sale(models.Model):
    """  
        Creates a new sale object
    """
    date = models.DateField(default=str(datetime.date.today()),verbose_name=_('Date of sale'),null=False,blank=False)
    product = models.ForeignKey(Product,verbose_name=_('Product sold'),
              null=False,blank=False)
    quantity = models.PositiveIntegerField(verbose_name=_('Quantity'),
            blank=False,null=False,default=0)
    subtotal_amount = models.PositiveIntegerField(verbose_name=_('Subtotal Amount'),
                      blank=False,null=False,default=0.00)
    shipping_fees = models.FloatField(verbose_name=_('Shipping fees'),
            blank=False,null=False,default=0.00)
    additional_fees = models.FloatField(verbose_name=_('Additional fees'),
            blank=False,null=False,default=0.00 )
    description = models.CharField(verbose_name=_('Description'),
            blank=True,null=True,max_length=500)
    total_amount = models.PositiveIntegerField(verbose_name=_('Total Amount'),
            blank=False,null=False,default=0.00 )
