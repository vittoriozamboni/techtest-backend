from django.contrib.auth.models import User
from django.db import models

import tagulous


class Owner(models.Model):
    name = models.CharField(max_length=100)
    website = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class SocialMedia(models.Model):
    name = models.CharField(max_length=100)
    website = models.CharField(max_length=200)
    owner = models.ForeignKey(Owner, related_name='social_media')

    def __str__(self):
        return self.name


class ContentType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(default='')
    category = models.ForeignKey(Category, related_name='posts')
    tags = tagulous.models.TagField()
    content_types = models.ManyToManyField(ContentType, related_name='posts')
    social_media = models.ForeignKey(SocialMedia, related_name='posts')

    creation_datetime = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='posts')
    last_change_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
