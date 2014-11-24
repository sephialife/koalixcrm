from reporting.models import CustomerReport
from model_report.report import reports, ReportAdmin
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
import os.path

"""
    Those classes uses django-model-report
    to creates reports from models
"""

class CustomerReport(ReportAdmin):
    """ creates reports from customers """

    title = _('Customer-Reports') 
    model = CustomerReport
    base_template_name=os.path.join(settings.TEMPLATE_DIRS[0],'x.html')
    chart_types=('pie','column','line')
    fields = [
        #'id',
        'effective_date',
        'effective_date__year',
        'effective_date__month',
        'effective_date__day',
        'customer_acquisition',
        'customer_lost'
    ]
    list_filter = ('customer_acquisition')
    list_group_by = ('effective_date__month','effective_date__year','effective_date__day')
    list_order_by = ('effective_date__month','effective_date__year','effective_date__day')
    list_serie_fields = ('customer_acquisition','customer_lost')
    type = 'chart'

    override_field_labels = {
        'effective_date_year': _('year'),
        'effective_date_month': _('month'),
        'effective_date_month': _('month')
            }

reports.register('customer-reports' , CustomerReport)
