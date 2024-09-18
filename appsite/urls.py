from appsite.settings import DEBUG

from django.contrib import admin
from django.urls import include, path

from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('catalog/', include('goods.urls', namespace='catalog')),
    
]

if DEBUG:
    urlpatterns += [
    
    ] + debug_toolbar_urls()
