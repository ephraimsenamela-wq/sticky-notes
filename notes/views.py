from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from .models import Note
from .forms import NoteForm


class NoteListView(ListView):
    """Read (all): board view of every sticky note."""

    model = Note
    template_name = "notes/note_list.html"
    context_object_name = "notes"


class NoteDetailView(DetailView):
    """Read (one): single sticky note."""

    model = Note
    template_name = "notes/note_detail.html"
    context_object_name = "note"


class NoteCreateView(CreateView):
    """Create a new sticky note."""

    model = Note
    form_class = NoteForm
    template_name = "notes/note_form.html"
    success_url = reverse_lazy("notes:note-list")


class NoteUpdateView(UpdateView):
    """Update / edit an existing sticky note."""

    model = Note
    form_class = NoteForm
    template_name = "notes/note_form.html"
    success_url = reverse_lazy("notes:note-list")


class NoteDeleteView(DeleteView):
    """Delete a sticky note (with confirmation)."""

    model = Note
    template_name = "notes/note_confirm_delete.html"
    success_url = reverse_lazy("notes:note-list")
