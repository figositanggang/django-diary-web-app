from django.shortcuts import render, redirect
from django.contrib.auth import logout

from .forms import SignupForm


def signup(req):
    form = SignupForm

    if req.method == "POST":
        form = SignupForm(req.POST)

        if form.is_valid():
            form.save()

            return redirect("../login/")

    return render(req, "user/signup.html", {"form": form})


def logout_view(req):
    logout(req)

    return redirect("/")
