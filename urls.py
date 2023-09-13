from django.urls import re_path

import ceom.flux.views



urlpatterns = [
    re_path(r'^$', ceom.flux.views.index),
    re_path(r'^siteselect/$', ceom.flux.views.siteselect),
    re_path(r'^recentsite/$', ceom.flux.views.recentsite),
    re_path(r'^site/$', ceom.flux.views.site),
    re_path(r'^upload/$', ceom.flux.views.upload),
    re_path(r'^download/$', ceom.flux.views.download),
    re_path(r'^simulation/$', ceom.flux.views.simulation),

]
