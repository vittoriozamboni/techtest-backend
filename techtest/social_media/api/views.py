from rest_framework import viewsets

from .. import models
import serializers


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.User.objects.all().order_by('last_name', 'first_name')
    serializer_class = serializers.UserSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Owner.objects.all().order_by('name')
    serializer_class = serializers.OwnerSerializer


class SocialMediaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.SocialMedia.objects.all().order_by('name')
    serializer_class = serializers.SocialMediaSerializer


class ContentTypeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows ContentTypes to be viewed or edited.
    """
    queryset = models.ContentType.objects.all().order_by('name')
    serializer_class = serializers.ContentTypeSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Categorys to be viewed or edited.
    """
    queryset = models.Category.objects.all().order_by('name')
    serializer_class = serializers.CategorySerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Posts to be viewed or edited.
    """
    queryset = models.Post.objects.all().order_by('creation_datetime')
    serializer_class = serializers.PostSerializer
