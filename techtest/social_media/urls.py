from django.conf.urls import include, url


urlpatterns = [
    url(r'^api/', include('social_media.api.urls', namespace='social_media_api'))
]
