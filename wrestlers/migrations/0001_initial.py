# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'WrestlingEntity'
        db.create_table('wrestlers_wrestlingentity', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('wrestlers', ['WrestlingEntity'])

        # Adding model 'Group'
        db.create_table('wrestlers_group', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=128)),
        ))
        db.send_create_signal('wrestlers', ['Group'])

        # Adding M2M table for field wrestlers on 'Group'
        db.create_table('wrestlers_group_wrestlers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('group', models.ForeignKey(orm['wrestlers.group'], null=False)),
            ('wrestler', models.ForeignKey(orm['wrestlers.wrestler'], null=False))
        ))
        db.create_unique('wrestlers_group_wrestlers', ['group_id', 'wrestler_id'])

        # Adding model 'WrestlingTeam'
        db.create_table('wrestlers_wrestlingteam', (
            ('group_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['wrestlers.Group'], unique=True)),
            ('wrestlingentity_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['wrestlers.WrestlingEntity'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('wrestlers', ['WrestlingTeam'])

        # Adding model 'Wrestler'
        db.create_table('wrestlers_wrestler', (
            ('wrestlingentity_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['wrestlers.WrestlingEntity'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('wrestlers', ['Wrestler'])


    def backwards(self, orm):
        
        # Deleting model 'WrestlingEntity'
        db.delete_table('wrestlers_wrestlingentity')

        # Deleting model 'Group'
        db.delete_table('wrestlers_group')

        # Removing M2M table for field wrestlers on 'Group'
        db.delete_table('wrestlers_group_wrestlers')

        # Deleting model 'WrestlingTeam'
        db.delete_table('wrestlers_wrestlingteam')

        # Deleting model 'Wrestler'
        db.delete_table('wrestlers_wrestler')


    models = {
        'wrestlers.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'wrestlers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['wrestlers.Wrestler']", 'symmetrical': 'False'})
        },
        'wrestlers.wrestler': {
            'Meta': {'object_name': 'Wrestler', '_ormbases': ['wrestlers.WrestlingEntity']},
            'wrestlingentity_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['wrestlers.WrestlingEntity']", 'unique': 'True', 'primary_key': 'True'})
        },
        'wrestlers.wrestlingentity': {
            'Meta': {'object_name': 'WrestlingEntity'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        },
        'wrestlers.wrestlingteam': {
            'Meta': {'object_name': 'WrestlingTeam', '_ormbases': ['wrestlers.WrestlingEntity', 'wrestlers.Group']},
            'group_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['wrestlers.Group']", 'unique': 'True'}),
            'wrestlingentity_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['wrestlers.WrestlingEntity']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['wrestlers']
