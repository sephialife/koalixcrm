# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'CustomerReport'
        db.create_table(u'reporting_customerreport', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('effective_date', self.gf('django.db.models.fields.DateField')(default='2014-11-21')),
            ('customer_acquisition', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('customer_lost', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'reporting', ['CustomerReport'])


    def backwards(self, orm):
        # Deleting model 'CustomerReport'
        db.delete_table(u'reporting_customerreport')


    models = {
        u'reporting.customerreport': {
            'Meta': {'object_name': 'CustomerReport'},
            'customer_acquisition': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'customer_lost': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'effective_date': ('django.db.models.fields.DateField', [], {'default': "'2014-11-21'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['reporting']