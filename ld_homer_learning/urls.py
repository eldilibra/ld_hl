from django.conf.urls import patterns, include, url
from django.contrib import admin

from ld_homer_learning import views

urlpatterns = patterns('',
    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'.*', views.index, name='index'),
)
