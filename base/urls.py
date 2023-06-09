from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("tasks/", include("tasks.urls")),
    path("users/", include("users.urls")),
    path("users/", include("django.contrib.auth.urls")),
    path("", include("pages.urls")),
]

if settings.DEBUG:
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))
