from django.contrib import admin
from django.urls import path, include, re_path
from django.shortcuts import redirect


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('blog.urls', 'blog'), namespace='blog')),
    path('pages/', include(('pages.urls', 'pages'), namespace='pages')),
    re_path(r'^.*$', lambda request: redirect('/')),
]
