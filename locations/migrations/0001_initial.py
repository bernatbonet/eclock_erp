# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Via'
        db.create_table('locations_via', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cod', self.gf('django.db.models.fields.CharField')(unique=True, max_length=2)),
            ('desc', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
        ))
        db.send_create_signal('locations', ['Via'])

        # Adding model 'Pais'
        db.create_table('locations_pais', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cod', self.gf('django.db.models.fields.CharField')(unique=True, max_length=2)),
            ('codiso', self.gf('django.db.models.fields.CharField')(unique=True, max_length=3)),
            ('ue', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('desc', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal('locations', ['Pais'])

        # Adding model 'Provincia'
        db.create_table('locations_provincia', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cod', self.gf('django.db.models.fields.CharField')(unique=True, max_length=2)),
            ('desc', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('pais', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['locations.Pais'])),
        ))
        db.send_create_signal('locations', ['Provincia'])

        # Adding model 'Municipio'
        db.create_table('locations_municipio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cod', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('desc', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('provincia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['locations.Provincia'])),
        ))
        db.send_create_signal('locations', ['Municipio'])

        # Adding model 'Datos'
        db.create_table('locations_datos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('apellidos', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('edad', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('locations', ['Datos'])


    def backwards(self, orm):
        # Deleting model 'Via'
        db.delete_table('locations_via')

        # Deleting model 'Pais'
        db.delete_table('locations_pais')

        # Deleting model 'Provincia'
        db.delete_table('locations_provincia')

        # Deleting model 'Municipio'
        db.delete_table('locations_municipio')

        # Deleting model 'Datos'
        db.delete_table('locations_datos')


    models = {
        'locations.datos': {
            'Meta': {'object_name': 'Datos'},
            'apellidos': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'edad': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'locations.municipio': {
            'Meta': {'object_name': 'Municipio'},
            'cod': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'provincia': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['locations.Provincia']"})
        },
        'locations.pais': {
            'Meta': {'object_name': 'Pais'},
            'cod': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'}),
            'codiso': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '3'}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ue': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'locations.provincia': {
            'Meta': {'object_name': 'Provincia'},
            'cod': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['locations.Pais']"})
        },
        'locations.via': {
            'Meta': {'object_name': 'Via'},
            'cod': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '2'}),
            'desc': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['locations']