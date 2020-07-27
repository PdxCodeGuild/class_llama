
from django import forms

from .models import Grocery_List

class ListForm(forms.ModelForm):

    class Meta:
        model = Grocery_List
        fields = ('Item', '',)
