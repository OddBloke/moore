# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding M2M table for field data_sources on 'Wrestler'
        db.create_table('wrestlers_wrestler_data_sources', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('wrestler', models.ForeignKey(orm['wrestlers.wrestler'], null=False)),
            ('sourcingdescription', models.ForeignKey(orm['data_sources.sourcingdescription'], null=False))
        ))
        db.create_unique('wrestlers_wrestler_data_sources', ['wrestler_id', 'sourcingdescription_id'])

        # Adding M2M table for field data_sources on 'WrestlingEntity'
        db.create_table('wrestlers_wrestlingentity_data_sources', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('wrestlingentity', models.ForeignKey(orm['wrestlers.wrestlingentity'], null=False)),
            ('sourcingdescription', models.ForeignKey(orm['data_sources.sourcingdescription'], null=False))
        ))
        db.create_unique('wrestlers_wrestlingentity_data_sources', ['wrestlingentity_id', 'sourcingdescription_id'])


    def backwards(self, orm):
        
        # Removing M2M table for field data_sources on 'Wrestler'
        db.delete_table('wrestlers_wrestler_data_sources')

        # Removing M2M table for field data_sources on 'WrestlingEntity'
        db.delete_table('wrestlers_wrestlingentity_data_sources')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
        'wrestlers.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'wrestlers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['wrestlers.Persona']", 'symmetrical': 'False'})
        },
        'wrestlers.persona': {
            'Meta': {'object_name': 'Persona', '_ormbases': ['wrestlers.WrestlingEntity']},
            'billed_height': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'billed_weight': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'debut': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'wrestler': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wrestlers.Wrestler']"}),
            'wrestlingentity_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['wrestlers.WrestlingEntity']", 'unique': 'True', 'primary_key': 'True'})
        },
        'wrestlers.wrestler': {
            'Meta': {'object_name': 'Wrestler'},
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'born_location': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'born_when': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'data_sources': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['data_sources.SourcingDescription']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'reviewed_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'reviewed_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'trained_by': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['wrestlers.Wrestler']", 'symmetrical': 'False', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'wrestlers.wrestlingentity': {
            'Meta': {'object_name': 'WrestlingEntity'},
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'data_sources': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['data_sources.SourcingDescription']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'reviewed_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'reviewed_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'wrestlers.wrestlingteam': {
            'Meta': {'object_name': 'WrestlingTeam', '_ormbases': ['wrestlers.WrestlingEntity', 'wrestlers.Group']},
            'group_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['wrestlers.Group']", 'unique': 'True'}),
            'wrestlingentity_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['wrestlers.WrestlingEntity']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['wrestlers']
