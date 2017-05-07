from .common import *

INSTALLED_APPS += [
    'corsheaders',
    'django_extensions',
    'tagulous',
    'rest_framework',
    'taggit_serializer',

    'social_media',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware', # CORS
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    #'DEFAULT_PERMISSION_CLASSES': [
    #    'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    #],
    'PAGE_SIZE': 10
}

CORS_ORIGIN_WHITELIST = (
    'localhost:8080',  # vue default port
    'localhost:4200',  # angular default port
)

# Tagolous
SERIALIZATION_MODULES = {
    'json':   'tagulous.serializers.json',
    'python': 'tagulous.serializers.python',
}