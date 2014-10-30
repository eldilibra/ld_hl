from django.conf.urls import patterns, url

from courses import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # ex: /courses/5/
    url(r'^(?P<course_id>\d+)/$', views.detail, name='detail'),
    url(r'^cart$', views.cart, name='cart'),
    url(r'^purchases/$', views.purchases, name='purchases'),

)
