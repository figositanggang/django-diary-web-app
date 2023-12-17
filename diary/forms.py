from django import forms

from .models import Diary


class CreateDiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ("title", "diary")
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "border-2 border-gray-700 rounded-md px-2 py-1 w-full xl:w-1/2 lg:w-1/2",
                    "placeholder": "Title",
                },
            ),
            "diary": forms.Textarea(
                attrs={
                    "class": "border-2 border-gray-700 rounded-md px-2 py-1 w-full xl:w-1/2 lg:w-1/2",
                    "placeholder": "Diary",
                },
            ),
        }
