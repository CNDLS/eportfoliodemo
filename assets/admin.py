from django.contrib import admin
from eportfoliodemo.assets.models import CustomMetaData, Asset, FileType

admin.site.register(FileType)
admin.site.register(CustomMetaData)
admin.site.register(Asset)