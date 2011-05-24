# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding M2M table for field data_sources on 'TitleName'
        db.create_table('promotions_titlename_data_sources', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('titlename', models.ForeignKey(orm['promotions.titlename'], null=False)),
            ('sourcingdescription', models.ForeignKey(orm['data_sources.sourcingdescription'], null=False))
        ))
        db.create_unique('promotions_titlename_data_sources', ['titlename_id', 'sourcingdescription_id'])

        # Adding M2M table for field data_sources on 'TitlePromotion'
        db.create_table('promotions_titlepromotion_data_sources', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('titlepromotion', models.ForeignKey(orm['promotions.titlepromotion'], null=False)),
            ('sourcingdescription', models.ForeignKey(orm['data_sources.sourcingdescription'], null=False))
        ))
        db.create_unique('promotions_titlepromotion_data_sources', ['titlepromotion_id', 'sourcingdescription_id'])

        # Adding M2M table for field data_sources on 'PromotionName'
        db.create_table('promotions_promotionname_data_sources', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('promotionname', models.ForeignKey(orm['promotions.promotionname'], null=False)),
            ('sourcingdescription', models.ForeignKey(orm['data_sources.sourcingdescription'], null=False))
        ))
        db.create_unique('promotions_promotionname_data_sources', ['promotionname_id', 'sourcingdescription_id'])


    def backwards(self, orm):
        
        # Removing M2M table for field data_sources on 'TitleName'
        db.delete_table('promotions_titlename_data_sources')

        # Removing M2M table for field data_sources on 'TitlePromotion'
        db.delete_table('promotions_titlepromotion_data_sources')

        # Removing M2M table for field data_sources on 'PromotionName'
        db.delete_table('promotions_promotionname_data_sources')


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
        },
        'promotions.promotion': {
            'Meta': {'object_name': 'Promotion'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        'promotions.promotionname': {
            'Meta': {'unique_together': "(('obj', 'start_date'), ('obj', 'end_date'))", 'object_name': 'PromotionName'},
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'data_sources': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['data_sources.SourcingDescription']", 'symmetrical': 'False'}),
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
            'data_sources': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['data_sources.SourcingDescription']", 'symmetrical': 'False'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'obj': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'names'", 'to': "orm['promotions.Title']"}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        'promotions.titlepromotion': {
            'Meta': {'unique_together': "(('obj', 'start_date'), ('obj', 'end_date'))", 'object_name': 'TitlePromotion'},
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'data_sources': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['data_sources.SourcingDescription']", 'symmetrical': 'False'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'obj': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'promotions'", 'to': "orm['promotions.Title']"}),
            'promotion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['promotions.Promotion']"}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['promotions']
