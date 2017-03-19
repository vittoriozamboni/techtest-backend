# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-19 10:39
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import migrations


def create_superuser():
    superuser = User()
    superuser.is_active = True
    superuser.is_superuser = True
    superuser.is_staff = True
    superuser.username = 'admin'
    superuser.email = 'admin@admin.net'
    superuser.set_password('techtest2017')
    superuser.save()


def create_user(username, first_name, last_name):
    u = User(username=username, first_name=first_name, last_name=last_name)
    u.set_password('techtest2017')
    u.save()


def initial_data(apps, schema_editor):
    create_superuser()
    create_user('baggio', "Davide", "Baggio")
    create_user('rossi', "Mario", "Rossi")
    create_user('verdi', "Giorgio", "Verdi")
    create_user('zamboni', "Vittorio", "Zamboni")

    Owner = apps.get_model("social_media", "Owner")
    facebook = Owner(name="Facebook, Inc.", website="http://www.facebook.com")
    facebook.save()
    linkedin = Owner(name="LinkedIn Corporation", website="http://www.linkedin.com")
    linkedin.save()
    twitter = Owner(name="Twitter Inc.", website="http://www.twitter.com")
    twitter.save()

    SocialMedia = apps.get_model("social_media", "SocialMedia")
    SocialMedia.objects.create(name="Facebook", website="http://www.facebook.com", owner=facebook)
    SocialMedia.objects.create(name="LinkedIn", website="http://www.linkedin.com", owner=linkedin)
    SocialMedia.objects.create(name="Twitter", website="http://www.twitter.com", owner=twitter)

    ContentType = apps.get_model("social_media", "ContentType")
    ContentType.objects.create(name="Video")
    ContentType.objects.create(name="Picture")
    ContentType.objects.create(name="Story")
    ContentType.objects.create(name="Music")

    Category = apps.get_model("social_media", "Category")
    Category.objects.create(name="Sport")
    Category.objects.create(name="Music")
    Category.objects.create(name="Work")
    Category.objects.create(name="Technology")
    Category.objects.create(name="Photography")


class Migration(migrations.Migration):

    dependencies = [
        ('social_media', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(initial_data)
    ]
