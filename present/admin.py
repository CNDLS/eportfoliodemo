from django.contrib import admin
from eportfoliodemo.present.models import Page, Template, Project, ProjectType

admin.site.register(Page)
admin.site.register(Template)
admin.site.register(ProjectType)
admin.site.register(Project)