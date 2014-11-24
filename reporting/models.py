from django.db import models
import datetime
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class CustomerReport(models.Model): 
   effective_date = models.DateField(_('Date'),default=str(datetime.date.today())) 
   customer_acquisition = models.BooleanField(_('Customer acquisition'),default=True)
   customer_lost = models.BooleanField(_('Customer lost'),default=False)

   class Meta():
        verbose_name = _('Customer Report')
        verbose_name_plural = _('Customers Reports')
        permissions = (
            ('report_customer', 'Can create reports'),
        )

