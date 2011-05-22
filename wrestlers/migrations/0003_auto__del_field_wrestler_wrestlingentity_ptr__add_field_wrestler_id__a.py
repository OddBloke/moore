# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Wrestler.wrestlingentity_ptr'
        db.delete_column('wrestlers_wrestler', 'wrestlingentity_ptr_id')

        # Adding field 'Wrestler.id'
        db.add_column('wrestlers_wrestler', 'id', self.gf('django.db.models.fields.AutoField')(default=0, primary_key=True), keep_default=False)

        # Adding field 'Wrestler.reviewed_by'
        db.add_column('wrestlers_wrestler', 'reviewed_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True), keep_default=False)

        # Adding field 'Wrestler.reviewed_at'
        db.add_column('wrestlers_wrestler', 'reviewed_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True), keep_default=False)

        # Adding field 'Wrestler.updated_at'
        db.add_column('wrestlers_wrestler', 'updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2011, 5, 22, 3, 4, 11, 637032), blank=True), keep_default=False)

        # Deleting field 'Persona.reviewed_at'
        db.delete_column('wrestlers_persona', 'reviewed_at')

        # Deleting field 'Persona.reviewed_by'
        db.delete_column('wrestlers_persona', 'reviewed_by_id')

        # Deleting field 'Persona.updated_at'
        db.delete_column('wrestlers_persona', 'updated_at')

        # Deleting field 'Persona.id'
        db.delete_column('wrestlers_persona', 'id')

        # Adding field 'Persona.wrestlingentity_ptr'
        db.add_column('wrestlers_persona', 'wrestlingentity_ptr', self.gf('django.db.models.fields.related.OneToOneField')(default=0, to=orm['wrestlers.WrestlingEntity'], unique=True, primary_key=True), keep_default=False)


    def backwards(self, orm):
        
        # User chose to not deal with backwards NULL issues for 'Wrestler.wrestlingentity_ptr'
        raise RuntimeError("Cannot reverse this migration. 'Wrestler.wrestlingentity_ptr' and its values cannot be restored.")

        # Deleting field 'Wrestler.id'
        db.delete_column('wrestlers_wrestler', 'id')

        # Deleting field 'Wrestler.reviewed_by'
        db.delete_column('wrestlers_wrestler', 'reviewed_by_id')

        # Deleting field 'Wrestler.reviewed_at'
        db.delete_column('wrestlers_wrestler', 'reviewed_at')

        # Deleting field 'Wrestler.updated_at'
        db.delete_column('wrestlers_wrestler', 'updated_at')

        # Adding field 'Persona.reviewed_at'
        db.add_column('wrestlers_persona', 'reviewed_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True), keep_default=False)

        # Adding field 'Persona.reviewed_by'
        db.add_column('wrestlers_persona', 'reviewed_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True), keep_default=False)

        # Adding field 'Persona.updated_at'
        db.add_column('wrestlers_persona', 'updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2011, 5, 22, 3, 4, 25, 400908), blank=True), keep_default=False)

        # User chose to not deal with backwards NULL issues for 'Persona.id'
        raise RuntimeError("Cannot reverse this migration. 'Persona.id' and its values cannot be restored.")

        # Deleting field 'Persona.wrestlingentity_ptr'
        db.delete_column('wrestlers_persona', 'wrestlingentity_ptr_id')


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
        'wrestlers.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'wrestlers': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['wrestlers.Wrestler']", 'symmetrical': 'False'})
        },
        'wrestlers.persona': {
            'Meta': {'object_name': 'Persona', '_ormbases': ['wrestlers.WrestlingEntity']},
            'billed_height': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'billed_name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'billed_weight': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'debut': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'wrestler': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wrestlers.Wrestler']"}),
            'wrestlingentity_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['wrestlers.WrestlingEntity']", 'unique': 'True', 'primary_key': 'True'})
        },
        'wrestlers.wrestler': {
            'Meta': {'object_name': 'Wrestler'},
            'born_location': ('django.db.models.fields.CharField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'born_when': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'reviewed_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'reviewed_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'trained_by': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['wrestlers.Wrestler']", 'symmetrical': 'False', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
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
