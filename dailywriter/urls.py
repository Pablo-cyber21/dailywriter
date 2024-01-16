from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("daily_writer_app.urls")),
    path("new_entry", include("daily_writer_app.urls")),
    path("", include("django.contrib.auth.urls")),
    path("edit_entry", include("daily_writer_app.urls")),
]
