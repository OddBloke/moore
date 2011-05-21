# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Card'
        db.create_table('matches_card', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('promotion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['promotions.Promotion'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=127, null=True, blank=True)),
        ))
        db.send_create_signal('matches', ['Card'])

        # Adding model 'Role'
        db.create_table('matches_role', (
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, primary_key=True)),
        ))
        db.send_create_signal('matches', ['Role'])

        # Adding model 'Participation'
        db.create_table('matches_participation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.CardEvent'])),
            ('participant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['wrestlers.WrestlingEntity'])),
            ('role', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.Role'])),
        ))
        db.send_create_signal('matches', ['Participation'])

        # Adding model 'EventType'
        db.create_table('matches_eventtype', (
            ('description', self.gf('django.db.models.fields.CharField')(max_length=127, primary_key=True)),
        ))
        db.send_create_signal('matches', ['EventType'])

        # Adding model 'CardEvent'
        db.create_table('matches_cardevent', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('reviewed_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('reviewed_at', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
            ('card', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.Card'])),
            ('event_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.EventType'])),
        ))
        db.send_create_signal('matches', ['CardEvent'])

        # Adding model 'MatchTypeAspect'
        db.create_table('matches_matchtypeaspect', (
            ('description', self.gf('django.db.models.fields.CharField')(max_length=127, primary_key=True)),
        ))
        db.send_create_signal('matches', ['MatchTypeAspect'])

        # Adding model 'MatchType'
        db.create_table('matches_matchtype', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=127)),
        ))
        db.send_create_signal('matches', ['MatchType'])

        # Adding M2M table for field aspects on 'MatchType'
        db.create_table('matches_matchtype_aspects', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('matchtype', models.ForeignKey(orm['matches.matchtype'], null=False)),
            ('matchtypeaspect', models.ForeignKey(orm['matches.matchtypeaspect'], null=False))
        ))
        db.create_unique('matches_matchtype_aspects', ['matchtype_id', 'matchtypeaspect_id'])

        # Adding model 'Match'
        db.create_table('matches_match', (
            ('cardevent_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['matches.CardEvent'], unique=True, primary_key=True)),
            ('match_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['matches.MatchType'])),
            ('winner', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='won_matches', null=True, to=orm['wrestlers.WrestlingEntity'])),
        ))
        db.send_create_signal('matches', ['Match'])


    def backwards(self, orm):
        
        # Deleting model 'Card'
        db.delete_table('matches_card')

        # Deleting model 'Role'
        db.delete_table('matches_role')

        # Deleting model 'Participation'
        db.delete_table('matches_participation')

        # Deleting model 'EventType'
        db.delete_table('matches_eventtype')

        # Deleting model 'CardEvent'
        db.delete_table('matches_cardevent')

        # Deleting model 'MatchTypeAspect'
        db.delete_table('matches_matchtypeaspect')

        # Deleting model 'MatchType'
        db.delete_table('matches_matchtype')

        # Removing M2M table for field aspects on 'MatchType'
        db.delete_table('matches_matchtype_aspects')

        # Deleting model 'Match'
        db.delete_table('matches_match')


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
        'matches.card': {
            'Meta': {'object_name': 'Card'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '127', 'null': 'True', 'blank': 'True'}),
            'promotion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['promotions.Promotion']"})
        },
        'matches.cardevent': {
            'Meta': {'object_name': 'CardEvent'},
            'card': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['matches.Card']"}),
            'event_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['matches.EventType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'participants': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['wrestlers.WrestlingEntity']", 'through': "orm['matches.Participation']", 'symmetrical': 'False'}),
            'reviewed_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'reviewed_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'matches.eventtype': {
            'Meta': {'object_name': 'EventType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '127', 'primary_key': 'True'})
        },
        'matches.match': {
            'Meta': {'object_name': 'Match', '_ormbases': ['matches.CardEvent']},
            'cardevent_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['matches.CardEvent']", 'unique': 'True', 'primary_key': 'True'}),
            'match_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['matches.MatchType']"}),
            'winner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'won_matches'", 'null': 'True', 'to': "orm['wrestlers.WrestlingEntity']"})
        },
        'matches.matchtype': {
            'Meta': {'object_name': 'MatchType'},
            'aspects': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['matches.MatchTypeAspect']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '127'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'matches.matchtypeaspect': {
            'Meta': {'object_name': 'MatchTypeAspect'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '127', 'primary_key': 'True'})
        },
        'matches.participation': {
            'Meta': {'object_name': 'Participation'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['matches.CardEvent']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'participant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['wrestlers.WrestlingEntity']"}),
            'role': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['matches.Role']"})
        },
        'matches.role': {
            'Meta': {'object_name': 'Role'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'})
        },
        'promotions.promotion': {
            'Meta': {'object_name': 'Promotion'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        'wrestlers.wrestlingentity': {
            'Meta': {'object_name': 'WrestlingEntity'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'})
        }
    }

    complete_apps = ['matches']
