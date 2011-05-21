# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):
    
    def forwards(self, orm):
        
        # Adding model 'Persona'
        db.create_table('wrestlers_persona', (
            ('reviewed_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('reviewed_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('billed_weight', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('debut', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('billed_height', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('billed_name', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('wrestler', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wrestlers.Wrestler'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('wrestlers', ['Persona'])

        # Adding field 'Wrestler.born_when'
        db.add_column('wrestlers_wrestler', 'born_when', self.gf('django.db.models.fields.DateField')(null=True, blank=True), keep_default=False)

        # Adding field 'Wrestler.born_location'
        db.add_column('wrestlers_wrestler', 'born_location', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True), keep_default=False)

        # Adding M2M table for field trained_by on 'Wrestler'
        db.create_table('wrestlers_wrestler_trained_by', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_wrestler', models.ForeignKey(orm['wrestlers.wrestler'], null=False)),
            ('to_wrestler', models.ForeignKey(orm['wrestlers.wrestler'], null=False))
        ))
        db.create_unique('wrestlers_wrestler_trained_by', ['from_wrestler_id', 'to_wrestler_id'])

        # Adding field 'WrestlingEntity.bio'
        db.add_column('wrestlers_wrestlingentity', 'bio', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'WrestlingEntity.reviewed_at'
        db.add_column('wrestlers_wrestlingentity', 'reviewed_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True), keep_default=False)

        # Adding field 'WrestlingEntity.reviewed_by'
        db.add_column('wrestlers_wrestlingentity', 'reviewed_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True), keep_default=False)

        # Adding field 'WrestlingEntity.updated_at'
        db.add_column('wrestlers_wrestlingentity', 'updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.date(2011, 5, 21), blank=True), keep_default=False)
    
    
    def backwards(self, orm):
        
        # Deleting model 'Persona'
        db.delete_table('wrestlers_persona')

        # Deleting field 'Wrestler.born_when'
        db.delete_column('wrestlers_wrestler', 'born_when')

        # Deleting field 'Wrestler.born_location'
        db.delete_column('wrestlers_wrestler', 'born_location')

        # Removing M2M table for field trained_by on 'Wrestler'
        db.delete_table('wrestlers_wrestler_trained_by')

        # Deleting field 'WrestlingEntity.bio'
        db.delete_column('wrestlers_wrestlingentity', 'bio')

        # Deleting field 'WrestlingEntity.reviewed_at'
        db.delete_column('wrestlers_wrestlingentity', 'reviewed_at')

        # Deleting field 'WrestlingEntity.reviewed_by'
        db.delete_column('wrestlers_wrestlingentity', 'reviewed_by_id')

        # Deleting field 'WrestlingEntity.updated_at'
        db.delete_column('wrestlers_wrestlingentity', 'updated_at')
    
    
    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
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
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'wrestlers.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'wrestlers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['wrestlers.Wrestler']", 'symmetrical': 'False'})
        },
        'wrestlers.persona': {
            'Meta': {'object_name': 'Persona'},
            'billed_height': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'billed_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'billed_weight': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'debut': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reviewed_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'reviewed_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'wrestler': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wrestlers.Wrestler']"})
        },
        'wrestlers.wrestler': {
            'Meta': {'object_name': 'Wrestler', '_ormbases': ['wrestlers.WrestlingEntity']},
            'born_location': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'born_when': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'trained_by': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['wrestlers.Wrestler']", 'symmetrical': 'False', 'blank': 'True'}),
            'wrestlingentity_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['wrestlers.WrestlingEntity']", 'unique': 'True', 'primary_key': 'True'})
        },
        'wrestlers.wrestlingentity': {
            'Meta': {'object_name': 'WrestlingEntity'},
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
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
