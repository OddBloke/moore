# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'DataSource'
        db.create_table('data_sources_datasource', (
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True)),
        ))
        db.send_create_signal('data_sources', ['DataSource'])

        # Adding model 'SourcingDescription'
        db.create_table('data_sources_sourcingdescription', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('data_source', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['data_sources.DataSource'])),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('data_sources', ['SourcingDescription'])


    def backwards(self, orm):
        
        # Deleting model 'DataSource'
        db.delete_table('data_sources_datasource')

        # Deleting model 'SourcingDescription'
        db.delete_table('data_sources_sourcingdescription')


    models = {
        'data_sources.datasource': {
            'Meta': {'object_name': 'DataSource'},
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'})
        },
        'data_sources.sourcingdescription': {
            'Meta': {'object_name': 'SourcingDescription'},
            'data_source': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['data_sources.DataSource']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['data_sources']
