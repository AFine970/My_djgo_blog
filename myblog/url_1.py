from django.conf.urls import url

from . import views
urlpatterns=[
    url(r'^blog/$', views.index, name='index'),
    url(r'^add/(?P<article_id>[0])/$', views.edit_page, name='add_page'),
    url(r'^show/$', views.showed, name='showed_page'),
    url(r'^change/(?P<article_id>[0-9]+)/$', views.edit_page, name='change_page'),
    url(r'^edit/action$', views.edit_action, name='edit_action'),
]