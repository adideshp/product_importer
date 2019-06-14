"""fulfil URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static


from app import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^upload/$', views.document_upload, name='document_upload'),
    url(r'^sse/post_event$', views.push_sse, name='push_sse'),
    #url(r'^uploads/simple/$', views.simple_upload, name='simple_upload'),
    #url(r'^adi/$', views.server_sent_events, name='server_sent_events'),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)