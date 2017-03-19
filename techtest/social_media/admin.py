from django.contrib import admin

# Register your models here.

import models

admin.site.register(models.Category)
admin.site.register(models.ContentType)
admin.site.register(models.Owner)
admin.site.register(models.Post)
admin.site.register(models.SocialMedia)
