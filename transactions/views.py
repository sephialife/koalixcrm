from django.shortcuts import render
from django.conf import settings
from extra_views import UpdateWithInlinesView, InlineFormSet, NamedFormsetsMixin, CreateWithInlinesView
from django.core.urlresolvers import reverse_lazy
from braces.views import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
# Create your views here.
