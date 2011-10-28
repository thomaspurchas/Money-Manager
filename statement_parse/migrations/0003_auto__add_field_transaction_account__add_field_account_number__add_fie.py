# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Transaction.account'
        db.add_column('statement_parse_transaction', 'account', self.gf('django.db.models.fields.related.ForeignKey')(default=0, to=orm['statement_parse.Account']), keep_default=False)

        # Adding field 'Account.number'
        db.add_column('statement_parse_account', 'number', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'Account.bank'
        db.add_column('statement_parse_account', 'bank', self.gf('django.db.models.fields.TextField')(default=''), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Transaction.account'
        db.delete_column('statement_parse_transaction', 'account_id')

        # Deleting field 'Account.number'
        db.delete_column('statement_parse_account', 'number')

        # Deleting field 'Account.bank'
        db.delete_column('statement_parse_account', 'bank')


    models = {
        'statement_parse.account': {
            'Meta': {'object_name': 'Account'},
            'bank': ('django.db.models.fields.TextField', [], {'default': "''"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'number': ('django.db.models.fields.IntegerField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'statement_parse.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'account': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['statement_parse.Account']"}),
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '20', 'decimal_places': '2'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['statement_parse']
