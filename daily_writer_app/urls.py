from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("new_entry/", views.new_entry, name="new_entry"),
    path("edit_entry/<int:entry_id>", views.edit_entry, name="edit_entry"),
    path("sign-up", views.sign_up, name="sign-up"),
]
