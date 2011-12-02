from django.contrib import admin
from eportfoliodemo.assets.models import CustomMetaData, Asset, FileType, AssetAlias

admin.site.register(FileType)
admin.site.register(CustomMetaData)
admin.site.register(Asset)
admin.site.register(AssetAlias)