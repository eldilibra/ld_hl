from django.contrib import admin
from courses.models import Course

admin.AdminSite.site_header = 'Homer Learning'
admin.site.register(Course)
