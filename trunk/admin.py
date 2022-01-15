from django.contrib import admin
from .models import Subject, Subject_Info, Subject_Extra_Info

admin.site.register(Subject)
admin.site.register(Subject_Info)
admin.site.register(Subject_Extra_Info)

admin.site.site_header = "ICivilisation Admin"
admin.site.site_title = "ICDRF Admin Portal"
admin.site.index_title = "Welcome to ICDRF Researcher Portal"