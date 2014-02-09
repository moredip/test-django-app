# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Car'
        db.create_table(u'main_car', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'main', ['Car'])

        # Adding model 'Kitty'
        db.create_table(u'main_kitty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('color', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'main', ['Kitty'])


    def backwards(self, orm):
        # Deleting model 'Car'
        db.delete_table(u'main_car')

        # Deleting model 'Kitty'
        db.delete_table(u'main_kitty')


    models = {
        u'main.car': {
            'Meta': {'object_name': 'Car'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'main.kitty': {
            'Meta': {'object_name': 'Kitty'},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['main']