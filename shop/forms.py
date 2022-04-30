from django import forms
from .models import Category, Store

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category

        fields = "__all__"

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control border-success mt-1 mb-4",
                    "placeholder": "Please enter name...",
                    "id": "name",
                },
            ),
            "description": forms.TextInput(
                attrs={
                    "class": "form-control border-success mt-1 mb-4",
                    "placeholder": "Please enter description...",
                    "id": "description",
                },
            ),
            
            
        }



class StoreForm(forms.ModelForm):
    class Meta:
        model = Store

        fields = "__all__"

        widgets = {
             "image": forms.TextInput(
                attrs={
                    "class": "form-control border-success mt-1 mb-4",
                    "placeholder": "Please enter image...",
                    "id": "image",
                },
            ),
             
            
            "code": forms.NumberInput(
                attrs={
                    "class": "form-control border-success mt-1 mb-4",
                    "placeholder": "Please enter code...",
                    "id": "code",
                },
            ),
            "name": forms.TextInput(
                attrs={
                    "class": "form-control border-success mt-1 mb-4",
                    "placeholder": "Please enter name...",
                    "id": "name",
                },
            ),
            "date": forms.DateInput(
                attrs={
                    "class": "form-control border-success mt-1 mb-4",
                    "placeholder": "Please enter date...",
                    "id": "date",
                },
            ),
            "price": forms.NumberInput(
                attrs={
                    "class": "form-control border-success mt-1 mb-4",
                    "placeholder": "Please enter price...",
                    "id": "price",
                },
            ),
            
            
            "category_id": forms.Select(
                attrs={
                    "class": "form-select border-success mt-1 mb-4",
                    "id": "category_id",
                },
            ),
        }
