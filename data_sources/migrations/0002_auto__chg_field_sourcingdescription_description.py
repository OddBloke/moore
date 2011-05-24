# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'SourcingDescription.description'
        db.alter_column('data_sources_sourcingdescription', 'description', self.gf('django.db.models.fields.TextField')(null=True))


    def backwards(self, orm):
        
        # User chose to not deal with backwards NULL issues for 'SourcingDescription.description'
        raise RuntimeError("Cannot reverse this migration. 'SourcingDescription.description' and its values cannot be restored.")


    models = {
        'data_sources.datasource': {
            'Meta': {'object_name': 'DataSource'},
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'})
        },
        'data_sources.sourcingdescription': {
            'Meta': {'object_name': 'SourcingDescription'},
            'data_source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data_sources.DataSource']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['data_sources']
