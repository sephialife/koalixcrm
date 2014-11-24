from django.shortcuts import render
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from braces.views import PermissionRequiredMixin, LoginRequiredMixin
# Create your views here.
from sales.models import Sale

class CreateSale(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Sale
    permission_required = 'sales.create_sale'
    login_url = settings.LOGIN_URL
    fields = ['date','product','quantity','subtotal_amount',
    'shipping_fees','additional_fees','description','total_amount']
    success_url = reverse_lazy('sale_list')

class ListSales(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Sale
    permission_required = 'sales.edit_sale'
    login_url = settings.LOGIN_URL
    fields = ['date','product','quantity','subtotal_amount',
    'shipping_fees','additional_fees','description','total_amount']

class EditSale(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Sale
    permission_required = 'sales.edit_sale'
    login_url = settings.LOGIN_URL
    fields = ['date','product','quantity','subtotal_amount',
    'shipping_fees','additional_fees','description','total_amount']
    success_url = reverse_lazy('sale_list')

class DeleteSale(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Sale
    permission_required = 'sales.edit_sale'
    login_url = settings.LOGIN_URL
    success_url = reverse_lazy('sale_list')

