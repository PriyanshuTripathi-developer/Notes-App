from django import forms
from .models import Note
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username' , 'email' , 'password1' , 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in ['username', 'password1', 'password2']:
            self.fields[field].help_text = None

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "content", "color", "pinned", "archived", "trashed", "reminder_at"]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter title"}),
            "content": forms.Textarea(attrs={"class": "form-control", "rows": 4, "placeholder": "Write your note here..."}),
            "color": forms.Select(attrs={"class": "form-select"}),
            "pinned": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "archived": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "trashed": forms.CheckboxInput(attrs={"class": "form-check-input"}),
            "reminder_at": forms.DateTimeInput(attrs={"class": "form-control", "type": "datetime-local"})
        }