# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'TitlePromotion'
        db.create_table('promotions_titlepromotion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('obj', self.gf('django.db.models.fields.related.ForeignKey')(related_name='promotions', to=orm['promotions.Title'])),
            ('promotion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['promotions.Promotion'])),
        ))
        db.send_create_signal('promotions', ['TitlePromotion'])


    def backwards(self, orm):
        
        # Deleting model 'TitlePromotion'
        db.delete_table('promotions_titlepromotion')


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
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        'promotions.titlename': {
            'Meta': {'object_name': 'TitleName'},
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'obj': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'names'", 'to': "orm['promotions.Title']"}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        'promotions.titlepromotion': {
            'Meta': {'object_name': 'TitlePromotion'},
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obj': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'promotions'", 'to': "orm['promotions.Title']"}),
            'promotion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['promotions.Promotion']"}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['promotions']
