from django.contrib import admin
from django.test import tag

from bugTrackerApp.models import *

# Register your models here.
admin.site.register(Project)
admin.site.register(bug_ticket)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(extendedUser)