from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include, url

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
]
