from rest_framework import serializers

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


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Post
        exclude = set()

