# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Product.sold'
        db.alter_column(u'crm_product', 'sold', self.gf('django.db.models.fields.IntegerField')())

    def backwards(self, orm):

        # Changing field 'Product.sold'
        db.alter_column(u'crm_product', 'sold', self.gf('django.db.models.fields.PositiveIntegerField')())

    models = {
        u'accounting.account': {
            'Meta': {'ordering': "['accountNumber']", 'object_name': 'Account'},
            'accountNumber': ('django.db.models.fields.IntegerField', [], {}),
            'accountType': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isACustomerPaymentAccount': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isProductInventoryActiva': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isopeninterestaccount': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isopenreliabilitiesaccount': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'originalAmount': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '20', 'decimal_places': '2'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
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
        u'crm.customergrouptransform': {
            'Meta': {'object_name': 'CustomerGroupTransform'},
            'factor': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fromCustomerGroup': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'db_reltransfromfromcustomergroup'", 'to': u"orm['crm.CustomerGroup']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Product']"}),
            'toCustomerGroup': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'db_reltransfromtocustomergroup'", 'to': u"orm['crm.CustomerGroup']"})
        },
        u'crm.emailaddress': {
            'Meta': {'object_name': 'EmailAddress'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'emailaddresses'", 'to': u"orm['crm.Contact']"}),
            'purpose1': ('django.db.models.fields.CharField', [], {'default': "'C'", 'max_length': '1'})
        },
        u'crm.invoice': {
            'Meta': {'object_name': 'Invoice', '_ormbases': [u'crm.SalesContract']},
            'derivatedFromQuote': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Quote']", 'null': 'True', 'blank': 'True'}),
            'payableuntil': ('django.db.models.fields.DateField', [], {}),
            'paymentBankReference': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'salescontract_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['crm.SalesContract']", 'unique': 'True', 'primary_key': 'True'}),
            'state': ('django_fsm.FSMIntegerField', [], {'default': '1'})
        },
        u'crm.phoneaddress': {
            'Meta': {'object_name': 'PhoneAddress'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'phonenumbers'", 'to': u"orm['crm.Contact']"}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'purpose1': ('django.db.models.fields.CharField', [], {'default': "'H'", 'max_length': '1'})
        },
        u'crm.position': {
            'Meta': {'object_name': 'Position'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'discount': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastCalculatedPrice': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '17', 'decimal_places': '2', 'blank': 'True'}),
            'lastCalculatedTax': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '17', 'decimal_places': '2', 'blank': 'True'}),
            'lastPricingDate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'overwriteProductPrice': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'positionNumber': ('django.db.models.fields.IntegerField', [], {}),
            'positionPricePerUnit': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '17', 'decimal_places': '2', 'blank': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Product']", 'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '3'}),
            'sentOn': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'shipmentID': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Supplier']", 'null': 'True', 'blank': 'True'}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Unit']", 'null': 'True', 'blank': 'True'})
        },
        u'crm.postaladdress': {
            'Meta': {'object_name': 'PostalAddress'},
            'addressline1': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'addressline2': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'addressline3': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'addressline4': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'person': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'addresses'", 'to': u"orm['crm.Contact']"}),
            'purpose1': ('django.db.models.fields.CharField', [], {'default': "'C'", 'max_length': '1'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'town': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'zipcode': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'crm.price': {
            'Meta': {'object_name': 'Price'},
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Currency']"}),
            'customerGroup': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.CustomerGroup']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '17', 'decimal_places': '2'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Product']"}),
            'unit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Unit']"}),
            'validfrom': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'validuntil': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'crm.product': {
            'Meta': {'object_name': 'Product'},
            'accoutingProductCategorie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['accounting.ProductCategory']", 'null': 'True', 'blank': "'True'"}),
            'dateofcreation': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'defaultunit': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Unit']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastmodification': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'lastmodifiedby': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': "'True'"}),
            'product_number': ('django.db.models.fields.IntegerField', [], {}),
            'product_price': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'sold': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'tax': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Tax']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'crm.purchaseorder': {
            'Meta': {'object_name': 'PurchaseOrder'},
            'contract': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Contract']"}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Currency']"}),
            'dateofcreation': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'externalReference': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastCalculatedPrice': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '17', 'decimal_places': '2', 'blank': 'True'}),
            'lastCalculatedTax': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '17', 'decimal_places': '2', 'blank': 'True'}),
            'lastPricingDate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'lastmodification': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'lastmodifiedby': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'db_polstmodified'", 'to': u"orm['auth.User']"}),
            'staff': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'db_relpostaff'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'state': ('django_fsm.FSMIntegerField', [], {'default': '1'}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Supplier']"})
        },
        u'crm.purchaseorderposition': {
            'Meta': {'object_name': 'PurchaseOrderPosition', '_ormbases': [u'crm.Position']},
            'contract': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.PurchaseOrder']"}),
            u'position_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['crm.Position']", 'unique': 'True', 'primary_key': 'True'})
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
        u'crm.salescontractposition': {
            'Meta': {'object_name': 'SalesContractPosition', '_ormbases': [u'crm.Position']},
            'contract': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.SalesContract']"}),
            u'position_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['crm.Position']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'crm.supplier': {
            'Meta': {'object_name': 'Supplier', '_ormbases': [u'crm.Contact']},
            u'contact_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['crm.Contact']", 'unique': 'True', 'primary_key': 'True'}),
            'direct_shipment_to_customers': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'crm.tax': {
            'Meta': {'object_name': 'Tax'},
            'accountActiva': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'db_relaccountactiva'", 'null': 'True', 'to': u"orm['accounting.Account']"}),
            'accountPassiva': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'db_relaccountpassiva'", 'null': 'True', 'to': u"orm['accounting.Account']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'taxrate': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'})
        },
        u'crm.unit': {
            'Meta': {'object_name': 'Unit'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'factor': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fractionof': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Unit']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'shortname': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        u'crm.unittransform': {
            'Meta': {'object_name': 'UnitTransform'},
            'factor': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'fromUnit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'db_reltransfromfromunit'", 'to': u"orm['crm.Unit']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['crm.Product']"}),
            'toUnit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'db_reltransfromtounit'", 'to': u"orm['crm.Unit']"})
        }
    }

    complete_apps = ['crm']