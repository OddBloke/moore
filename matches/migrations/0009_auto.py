# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding M2M table for field data_sources on 'CardEvent'
        db.create_table('matches_cardevent_data_sources', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cardevent', models.ForeignKey(orm['matches.cardevent'], null=False)),
            ('sourcingdescription', models.ForeignKey(orm['data_sources.sourcingdescription'], null=False))
        ))
        db.create_unique('matches_cardevent_data_sources', ['cardevent_id', 'sourcingdescription_id'])

        # Adding M2M table for field data_sources on 'Card'
        db.create_table('matches_card_data_sources', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('card', models.ForeignKey(orm['matches.card'], null=False)),
            ('sourcingdescription', models.ForeignKey(orm['data_sources.sourcingdescription'], null=False))
        ))
        db.create_unique('matches_card_data_sources', ['card_id', 'sourcingdescription_id'])


    def backwards(self, orm):
        
        # Removing M2M table for field data_sources on 'CardEvent'
        db.delete_table('matches_cardevent_data_sources')

        # Removing M2M table for field data_sources on 'Card'
        db.delete_table('matches_card_data_sources')


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
        'matches.card': {
            'Meta': {'object_name': 'Card'},
            'broadcast_viewership': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'card_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['matches.CardType']"}),
            'data_sources': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['data_sources.SourcingDescription']", 'symmetrical': 'False'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'live_attendance': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '127', 'null': 'True', 'blank': 'True'}),
            'promotion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['promotions.Promotion']", 'symmetrical': 'False'}),
            'series': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['matches.CardSeries']", 'null': 'True', 'blank': 'True'}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['matches.Venue']", 'null': 'True', 'blank': 'True'})
        },
        'matches.cardevent': {
            'Meta': {'object_name': 'CardEvent'},
            'card': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['matches.Card']"}),
            'data_sources': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['data_sources.SourcingDescription']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'event_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['matches.EventType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order': ('django.db.models.fields.IntegerField', [], {}),
            'participants': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['wrestlers.WrestlingEntity']", 'through': "orm['matches.Participation']", 'symmetrical': 'False'}),
            'reviewed_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'reviewed_by': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'matches.cardseries': {
            'Meta': {'object_name': 'CardSeries'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '127'})
        },
        'matches.cardtype': {
            'Meta': {'object_name': 'CardType'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '127'})
        },
        'matches.eventtype': {
            'Meta': {'object_name': 'EventType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'})
        },
        'matches.match': {
            'Meta': {'object_name': 'Match', '_ormbases': ['matches.CardEvent']},
            'cardevent_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['matches.CardEvent']", 'unique': 'True', 'primary_key': 'True'}),
            'match_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['matches.MatchType']"}),
            'time': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'title_matches'", 'null': 'True', 'to': "orm['promotions.Title']"}),
            'win_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['matches.WinType']", 'null': 'True', 'blank': 'True'}),
            'winner': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'won_matches'", 'null': 'True', 'to': "orm['wrestlers.WrestlingEntity']"})
        },
        'matches.matchtype': {
            'Meta': {'object_name': 'MatchType'},
            'aspects': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['matches.MatchTypeAspect']", 'symmetrical': 'False', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '127'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'matches.matchtypeaspect': {
            'Meta': {'object_name': 'MatchTypeAspect'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'})
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
        'matches.venue': {
            'Meta': {'object_name': 'Venue'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '127'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '127'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '127'})
        },
        'matches.wintype': {
            'Meta': {'object_name': 'WinType'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'primary_key': 'True'})
        },
        'promotions.promotion': {
            'Meta': {'object_name': 'Promotion'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        'promotions.title': {
            'Meta': {'object_name': 'Title'},
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
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
        }
    }

    complete_apps = ['matches']