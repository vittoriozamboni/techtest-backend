from rest_framework import serializers

from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)

from .. import models


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = models.User
        fields = ('username', 'first_name', 'last_name', 'full_name')

    def get_full_name(self, user):
        return user.get_full_name()


class OwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Owner
        exclude = set()


class SocialMediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.SocialMedia
        exclude = set()


class ContentTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ContentType
        exclude = set()


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        exclude = set()


class TagField(serializers.ListField):

    """
    Color objects are serialized into 'rgb(#, #, #)' notation.
    """
    def to_representation(self, obj):
        return map(str, getattr(obj, self.source))

    def to_internal_value(self, data):
        return data


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = models.Post
        exclude = set()

