from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ld_homer_learning.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^admin/', include(admin.site.urls)),
)
