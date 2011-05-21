# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):

        # Renaming field 'Title.active_end_date' to 'Title.end_date'
        db.rename_column('promotions_title', 'active_end_date', 'end_date')

        # Renaming field 'Title.active_start_date' to 'Title.start_date'
        db.rename_column('promotions_title', 'active_start_date', 'start_date')


    def backwards(self, orm):

        # Renaming field 'Title.end_date' to 'Title.active_end_date'
        db.rename_column('promotions_title', 'end_date', 'active_end_date')

        # Renaming field 'Title.start_date' to 'Title.active_start_date'
        db.rename_column('promotions_title', 'start_date', 'active_start_date')


    models = {
        'promotions.promotion': {
            'Meta': {'object_name': 'Promotion'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        'promotions.promotionname': {
            'Meta': {'object_name': 'PromotionName'},
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'obj': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'names'", 'to': "orm['promotions.Promotion']"}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        'promotions.title': {
            'Meta': {'object_name': 'Title'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '127'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['promotions']
