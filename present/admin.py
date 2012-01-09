from django.contrib import admin
from eportfoliodemo.present.models import *

admin.site.register(Page)
admin.site.register(Template)
admin.site.register(ProjectType)
admin.site.register(Project)

admin.site.register(TemplateType)
# admin.site.register(Container)
# admin.site.register(ContainerItem)
admin.site.register(PageItem)