from django import forms
from .models import Todo
from django.forms import TextInput

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['item']
        widgets={
            'item': TextInput(
                attrs={
                    "type":"text",
                    "class":"form-control",
                    "aria-label":"Sizing example input",
                    "aria-describedby":"inputGroup-sizing-lg"
                }
            )
        }