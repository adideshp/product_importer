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
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

from app import views
router = routers.DefaultRouter()

router.register(r'products', views.ProductViewSet)

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^upload/$', views.document_upload, name='document_upload'),
    url(r'^sse/post_event$', views.push_sse, name='push_sse'),
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(router.urls)),
    url(r'^products/$', views.view_products, name='view_products'), 
    url(r'^products/update/(?P<sku>\w+[-\w+]*)/$', views.update_products_view, name='update_products_view'), 
    url(r'^products/add/$', views.add_new_product, name='add_new_product'), 
    url(r'^delete_all/$', views.delete_all, name='delete_all'), 

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)