# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AccountingPeriod'
        db.create_table(u'accounting_accountingperiod', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('begin', self.gf('django.db.models.fields.DateField')()),
            ('end', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'accounting', ['AccountingPeriod'])

        # Adding model 'Account'
        db.create_table(u'accounting_account', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('accountNumber', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('accountType', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('originalAmount', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=20, decimal_places=2)),
            ('current_balance', self.gf('django.db.models.fields.DecimalField')(default=0.0, max_digits=20, decimal_places=2)),
            ('isopenreliabilitiesaccount', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('isopeninterestaccount', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('isProductInventoryActiva', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('isACustomerPaymentAccount', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'accounting', ['Account'])

        # Adding model 'ProductCategory'
        db.create_table(u'accounting_productcategory', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('profitAccount', self.gf('django.db.models.fields.related.ForeignKey')(related_name='db_profit_account', to=orm['accounting.Account'])),
            ('lossAccount', self.gf('django.db.models.fields.related.ForeignKey')(related_name='db_loss_account', to=orm['accounting.Account'])),
        ))
        db.send_create_signal(u'accounting', ['ProductCategory'])

        # Adding model 'Booking'
        db.create_table(u'accounting_booking', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fromAccount', self.gf('django.db.models.fields.related.ForeignKey')(related_name='db_booking_fromaccount', to=orm['accounting.Account'])),
            ('toAccount', self.gf('django.db.models.fields.related.ForeignKey')(related_name='db_booking_toaccount', to=orm['accounting.Account'])),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=20, decimal_places=2)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('bookingReference', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['crm.Invoice'], null=True, blank=True)),
            ('bookingDate', self.gf('django.db.models.fields.DateTimeField')()),
            ('accountingPeriod', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['accounting.AccountingPeriod'])),
            ('staff', self.gf('django.db.models.fields.related.ForeignKey')(related_name='db_booking_refstaff', blank=True, to=orm['auth.User'])),
            ('dateOfCreation', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('lastModification', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('lastModifiedBy', self.gf('django.db.models.fields.related.ForeignKey')(related_name='db_booking_lstmodified', blank=True, to=orm['auth.User'])),
        ))
        db.send_create_signal(u'accounting', ['Booking'])


    def backwards(self, orm):
        # Deleting model 'AccountingPeriod'
        db.delete_table(u'accounting_accountingperiod')

        # Deleting model 'Account'
        db.delete_table(u'accounting_account')

        # Deleting model 'ProductCategory'
        db.delete_table(u'accounting_productcategory')

        # Deleting model 'Booking'
        db.delete_table(u'accounting_booking')


    models = {
        u'accounting.account': {
            'Meta': {'ordering': "['accountNumber']", 'object_name': 'Account'},
            'accountNumber': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'accountType': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'current_balance': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '20', 'decimal_places': '2'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isACustomerPaymentAccount': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isProductInventoryActiva': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isopeninterestaccount': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isopenreliabilitiesaccount': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'originalAmount': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '20', 'decimal_places': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'accounting.accountingaccount': {
            'Meta': {'object_name': 'AccountingAccount', 'db_table': "'accounting_account'", 'managed': 'False'},
            'accountnumber': ('django.db.models.fields.IntegerField', [], {'db_column': "'accountNumber'"}),
            'accounttype': ('django.db.models.fields.CharField', [], {'max_length': '1', 'db_column': "'accountType'"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'isacustomerpaymentaccount': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "'isACustomerPaymentAccount'"}),
            'isopeninterestaccount': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isopenreliabilitiesaccount': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isproductinventoryactiva': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_column': "'isProductInventoryActiva'"}),
            'originalamount': ('django.db.models.fields.DecimalField', [], {'db_column': "'originalAmount'", 'decimal_places': '5', 'max_digits': '10'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'accounting.accountingaccountingperiod': {
            'Meta': {'object_name': 'AccountingAccountingperiod', 'db_table': "'accounting_accountingperiod'", 'managed': 'False'},
            'begin': ('django.db.models.fields.DateField', [], {}),
            'end': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'accounting.accountingbooking': {
            'Meta': {'object_name': 'AccountingBooking', 'db_table': "'accounting_booking'", 'managed': 'False'},
            'accountingperiod': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounting.AccountingAccountingperiod']", 'db_column': "'accountingPeriod_id'"}),
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '5'}),
            'bookingdate': ('django.db.models.fields.DateTimeField', [], {'db_column': "'bookingDate'"}),
            'bookingreference_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'db_column': "'bookingReference_id'", 'blank': 'True'}),
            'dateofcreation': ('django.db.models.fields.DateTimeField', [], {'db_column': "'dateOfCreation'"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'fromaccount': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'fromacc'", 'db_column': "'fromAccount_id'", 'to': u"orm['accounting.AccountingAccount']"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'lastmodification': ('django.db.models.fields.DateTimeField', [], {'db_column': "'lastModification'"}),
            'lastmodifiedby_id': ('django.db.models.fields.IntegerField', [], {'db_column': "'lastModifiedBy_id'"}),
            'staff_id': ('django.db.models.fields.IntegerField', [], {}),
            'toaccount': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounting.AccountingAccount']", 'db_column': "'toAccount_id'"})
        },
        u'accounting.accountingperiod': {
            'Meta': {'object_name': 'AccountingPeriod'},
            'begin': ('django.db.models.fields.DateField', [], {}),
            'end': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'accounting.accountingproductcategory': {
            'Meta': {'object_name': 'AccountingProductcategory', 'db_table': "'accounting_productcategory'", 'managed': 'False'},
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'lossaccount': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounting.AccountingAccount']", 'db_column': "'lossAccount_id'"}),
            'profitaccount': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'profit'", 'db_column': "'profitAccount_id'", 'to': u"orm['accounting.AccountingAccount']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'accounting.booking': {
            'Meta': {'object_name': 'Booking'},
            'accountingPeriod': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounting.AccountingPeriod']"}),
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'bookingDate': ('django.db.models.fields.DateTimeField', [], {}),
            'bookingReference': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Invoice']", 'null': 'True', 'blank': 'True'}),
            'dateOfCreation': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'fromAccount': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'db_booking_fromaccount'", 'to': u"orm['accounting.Account']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastModification': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'lastModifiedBy': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'db_booking_lstmodified'", 'blank': 'True', 'to': u"orm['auth.User']"}),
            'staff': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'db_booking_refstaff'", 'blank': 'True', 'to': u"orm['auth.User']"}),
            'toAccount': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'db_booking_toaccount'", 'to': u"orm['accounting.Account']"})
        },
        u'accounting.productcategory': {
            'Meta': {'object_name': 'ProductCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lossAccount': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'db_loss_account'", 'to': u"orm['accounting.Account']"}),
            'profitAccount': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'db_profit_account'", 'to': u"orm['accounting.Account']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'crm.contact': {
            'Meta': {'object_name': 'Contact'},
            'dateofcreation': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastmodification': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'lastmodifiedby': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'prefix': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'})
        },
        u'crm.contract': {
            'Meta': {'object_name': 'Contract'},
            'dateofcreation': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'defaultSupplier': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Supplier']", 'null': 'True', 'blank': 'True'}),
            'defaultcurrency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Currency']"}),
            'defaultcustomer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Customer']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastmodification': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'lastmodifiedby': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'db_contractlstmodified'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'staff': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'db_relcontractstaff'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'crm.currency': {
            'Meta': {'object_name': 'Currency'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rounding': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'shortname': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        u'crm.customer': {
            'Meta': {'object_name': 'Customer', '_ormbases': [u'crm.Contact']},
            'billingcycle': ('django.db.models.fields.related.ForeignKey', [], {'default': '0', 'to': u"orm['crm.CustomerBillingCycle']", 'null': 'True'}),
            u'contact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['crm.Contact']", 'unique': 'True', 'primary_key': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'ismemberof': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['crm.CustomerGroup']", 'null': 'True', 'blank': 'True'})
        },
        u'crm.customerbillingcycle': {
            'Meta': {'object_name': 'CustomerBillingCycle'},
            'days_to_payment': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'crm.customergroup': {
            'Meta': {'object_name': 'CustomerGroup'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        u'crm.invoice': {
            'Meta': {'object_name': 'Invoice', '_ormbases': [u'crm.SalesContract']},
            'derivatedFromQuote': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Quote']", 'null': 'True', 'blank': 'True'}),
            'payableuntil': ('django.db.models.fields.DateField', [], {}),
            'paymentBankReference': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'salescontract_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['crm.SalesContract']", 'unique': 'True', 'primary_key': 'True'}),
            'state': ('django_fsm.FSMIntegerField', [], {'default': '1'})
        },
        u'crm.quote': {
            'Meta': {'object_name': 'Quote', '_ormbases': [u'crm.SalesContract']},
            u'salescontract_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['crm.SalesContract']", 'unique': 'True', 'primary_key': 'True'}),
            'state': ('django_fsm.FSMIntegerField', [], {'default': '1'}),
            'validuntil': ('django.db.models.fields.DateField', [], {})
        },
        u'crm.salescontract': {
            'Meta': {'object_name': 'SalesContract'},
            'contract': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Contract']"}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Currency']"}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Customer']"}),
            'dateofcreation': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'discount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'externalReference': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastCalculatedPrice': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '17', 'decimal_places': '2', 'blank': 'True'}),
            'lastCalculatedTax': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '17', 'decimal_places': '2', 'blank': 'True'}),
            'lastPricingDate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'lastmodification': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'lastmodifiedby': ('django.db.models.fields.related.ForeignKey', [], {'blank': "'True'", 'related_name': "'db_lstscmodified'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'staff': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'db_relscstaff'", 'null': 'True', 'to': u"orm['auth.User']"})
        },
        u'crm.supplier': {
            'Meta': {'object_name': 'Supplier', '_ormbases': [u'crm.Contact']},
            u'contact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['crm.Contact']", 'unique': 'True', 'primary_key': 'True'}),
            'direct_shipment_to_customers': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['accounting']