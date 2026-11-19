from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "content", "color"]
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Note title…"}
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 5,
                    "placeholder": "Write your sticky note content here…",
                }
            ),
            "color": forms.Select(attrs={"class": "form-select"}),
        }
