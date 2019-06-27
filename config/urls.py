from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include(('base.urls', 'base'), namespace='base')),
    path('admin/', admin.site.urls),
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),

]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
        path('django-rq/', include('django_rq.urls'))
    ] + urlpatterns
