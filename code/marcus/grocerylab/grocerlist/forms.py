<<<<<<< HEAD
from django import forms

from .models import Grocery_List

class ListForm(forms.ModelForm):

    class Meta:
        model = Grocery_List
        fields = ('Item', '',)
=======
from django import forms

from .models import Grocery_List

class ListForm(forms.ModelForm):

    class Meta:
        model = Grocery_List
        fields = ('Item', 'Description',)
>>>>>>> f3d370e3e894e7aaa988237f1ebaade842a9680c
