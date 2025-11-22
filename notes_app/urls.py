from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes_list, name="notes_list"),
    path('create/', views.create_note, name="create_note"),
    path('edit/<int:note_id>/', views.edit_note, name="edit_note"),
    path('delete/<int:note_id>/', views.delete_note, name="delete_note"),
    path('trash/', views.trash_list, name="trash_list"),
    path('trash/restore/<int:note_id>/', views.restore_note, name="restore_note"),
    path('trash/delete-permanent/<int:note_id>/', views.delete_permanently, name="delete_permanently"),
    path('pin/<int:note_id>/', views.toggle_pin, name="toggle_pin"),
    path('archive/<int:note_id>/', views.archive_note, name="archive_note"),
    path('archive/', views.archive_list, name="archive_list"),
    path('archive/restore/<int:note_id>/', views.restore_archived, name="restore_archived"),
    path("register/", views.register_view , name="register"),
    path("login/" , views.login_view , name="login"),
    path("logout/" , views.logout_view , name="logout"),
]