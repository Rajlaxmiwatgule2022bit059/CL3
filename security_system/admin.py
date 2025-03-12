from django.contrib import admin
from .models import User, Visitor, Incident, AccessLog

admin.site.register(User)
admin.site.register(Visitor)
admin.site.register(Incident)
admin.site.register(AccessLog)

