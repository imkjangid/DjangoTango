from django.urls import path
from signals import views

urlpatterns = [
    path('home/', views.index, name='index'),
    path('add_signal_user/', views.user_add, name='signal_user_add'),
    path('edit/<int:user_id>/', views.edit, name='signal_edit'),
    path('update/<int:user_id>/', views.user_update, name='signal_user_update'),
    path('delete/<int:user_id>/', views.user_delete, name='signal_user_delete'),
]