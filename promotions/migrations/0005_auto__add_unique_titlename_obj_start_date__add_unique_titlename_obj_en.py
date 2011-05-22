# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding unique constraint on 'TitleName', fields ['obj', 'start_date']
        db.create_unique('promotions_titlename', ['obj_id', 'start_date'])

        # Adding unique constraint on 'TitleName', fields ['obj', 'end_date']
        db.create_unique('promotions_titlename', ['obj_id', 'end_date'])

        # Adding unique constraint on 'TitlePromotion', fields ['obj', 'start_date']
        db.create_unique('promotions_titlepromotion', ['obj_id', 'start_date'])

        # Adding unique constraint on 'TitlePromotion', fields ['obj', 'end_date']
        db.create_unique('promotions_titlepromotion', ['obj_id', 'end_date'])

        # Adding unique constraint on 'PromotionName', fields ['obj', 'start_date']
        db.create_unique('promotions_promotionname', ['obj_id', 'start_date'])

        # Adding unique constraint on 'PromotionName', fields ['obj', 'end_date']
        db.create_unique('promotions_promotionname', ['obj_id', 'end_date'])


    def backwards(self, orm):
        
        # Removing unique constraint on 'PromotionName', fields ['obj', 'end_date']
        db.delete_unique('promotions_promotionname', ['obj_id', 'end_date'])

        # Removing unique constraint on 'PromotionName', fields ['obj', 'start_date']
        db.delete_unique('promotions_promotionname', ['obj_id', 'start_date'])

        # Removing unique constraint on 'TitlePromotion', fields ['obj', 'end_date']
        db.delete_unique('promotions_titlepromotion', ['obj_id', 'end_date'])

        # Removing unique constraint on 'TitlePromotion', fields ['obj', 'start_date']
        db.delete_unique('promotions_titlepromotion', ['obj_id', 'start_date'])

        # Removing unique constraint on 'TitleName', fields ['obj', 'end_date']
        db.delete_unique('promotions_titlename', ['obj_id', 'end_date'])

        # Removing unique constraint on 'TitleName', fields ['obj', 'start_date']
        db.delete_unique('promotions_titlename', ['obj_id', 'start_date'])


    models = {
        'promotions.promotion': {
            'Meta': {'object_name': 'Promotion'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        'promotions.promotionname': {
            'Meta': {'unique_together': "(('obj', 'start_date'), ('obj', 'end_date'))", 'object_name': 'PromotionName'},
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
            'Meta': {'unique_together': "(('obj', 'start_date'), ('obj', 'end_date'))", 'object_name': 'TitleName'},
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'obj': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'names'", 'to': "orm['promotions.Title']"}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        'promotions.titlepromotion': {
            'Meta': {'unique_together': "(('obj', 'start_date'), ('obj', 'end_date'))", 'object_name': 'TitlePromotion'},
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obj': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'promotions'", 'to': "orm['promotions.Title']"}),
            'promotion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['promotions.Promotion']"}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['promotions']
