from django.conf.urls import url, include

from rest_framework import routers

import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'owner', views.OwnerViewSet)
router.register(r'social-media', views.SocialMediaViewSet)
router.register(r'content-type', views.ContentTypeViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'post', views.PostViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]
