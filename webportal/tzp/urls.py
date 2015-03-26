# -*- coding: utf-8 -*-

u""" URL configs for TimeZonePresentation application """

from django.conf.urls import patterns, url

from tzp import views


urlpatterns = patterns(
    '',
    url(r'^$', views.single_view, name='tzp-single-view')
)
