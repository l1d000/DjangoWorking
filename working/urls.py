"""working URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
#import view
import rombuild.rom_build
import rombuild.views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles

urlpatterns = [
 #   url(r'^$', rombuild.views.default),
    url(r'^admin/', admin.site.urls),
    url(r'^index', rombuild.views.index),
    url(r'^login_user', rombuild.views.login_user),
    url(r'^logout_user', rombuild.views.logout_user),
    url(r'^running',rombuild.views.running),
    url(r'^get_progress', rombuild.rom_build.get_sync_progress),
    url(r'^animation.html', rombuild.views.animation),
    url(r'^base.html', rombuild.views.base),
    
    url(r'^resoult/(.+)/$', rombuild.views.project_build_out),
    url(r'^resoult', rombuild.views.project_build_father),
    url(r'^$', rombuild.views.default),
    url(r'^', rombuild.views.default),
]
urlpatterns += staticfiles_urlpatterns()
