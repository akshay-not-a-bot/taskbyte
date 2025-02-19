from django.shortcuts import render, redirect
from .forms import CustomRegisterForm
from django.contrib import messages

# Create your views here.


def account(request):
    context = {"acc_msg": "Hello, welcome to users page! Login or Register -->"}
    return render(request, "account.html", context)


def register(request):
    if request.method == "POST":
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, "User registration successful!")
        else:
            messages.error(request, "Error while registring the user!!!")
        return redirect("register")
    else:
        register_form = CustomRegisterForm()
        return render(request, "register.html", {"register_form": register_form})
