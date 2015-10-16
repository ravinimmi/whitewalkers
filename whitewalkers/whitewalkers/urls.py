"""whitewalkers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from apis import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^fetch_user_profile$', views.fetch_user_profile, name = 'get_user_profile'),
    url(r'^get_questions_panel$', views.get_questions_panel, name = 'get_questions_panel'),
    url(r'^get_question_data$', views.get_question_data, name = 'get_question_data'),
    url(r'^get_templates$', views.get_templates, name = 'get_templates'),
    url(r'^get_response$', views.get_response, name = 'get_response'),
    url(r'^push_question$', views.push_question, name = 'push_question'),
]
