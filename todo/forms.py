"""bazani modeli forms ni ichida yaratilinadi, database bilan ham shu yerda ishlatilinadi"""

from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"