from django.urls import path
from .views import (
    NoteCreateView,
    NoteDeleteView,
    NoteDetailView,
    NoteListView,
    NoteUpdateView,
)

app_name = "notes"

urlpatterns = [
    path("", NoteListView.as_view(), name="note-list"),
    path("note/<int:pk>/", NoteDetailView.as_view(), name="note-detail"),
    path("note/new/", NoteCreateView.as_view(), name="note-create"),
    path("note/<int:pk>/edit/", NoteUpdateView.as_view(), name="note-update"),
    path("note/<int:pk>/delete/", NoteDeleteView.as_view(), name="note-delete"),
]
