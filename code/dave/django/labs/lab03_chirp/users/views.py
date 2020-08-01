from django.shortcuts import render, redirect

from django.contrib import messages
from .forms import UserSignupForm

# Create your views here.
def signup(request):

   
    if request.method == 'POST':  # check if method was from 'POST'
        form = UserSignupForm(request.POST)
        if form.is_valid(): # if all form fields are valid create a new user
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('post-home')
    else:
        form = UserSignupForm() 
    return render(request, 'users/signup.html', {'form': form}) # show blank 'UserCreatForm'
