from django.urls import path
from basics import views

app_name = "basics"

urlpatterns = [
    path("basic_home/", views.index, name="index"),
    path("add/", views.user_add, name="user_add"),
    path("edit/<int:user_id>/", views.edit, name="edit"),
    path("update/<int:user_id>/", views.user_update, name="user_update"),
    path("delete/<int:user_id>/", views.user_delete, name="user_delete"),
]