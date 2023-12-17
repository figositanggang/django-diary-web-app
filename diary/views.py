from django.shortcuts import redirect, render
from django.contrib.auth.models import User

from .forms import CreateDiaryForm
from .models import Diary


# Create your views here.
def index(req):
    diaries = Diary.objects.filter(author=req.user).order_by("-created_at")

    return render(req, "diary/index.html", {"diaries": diaries})


def detail(req, pk):
    diary = Diary.objects.get(pk=pk)

    return render(req, "diary/detail.html", {"diary": diary})


def create(req):
    user = User.objects.get(pk=req.user.id)
    form = CreateDiaryForm(initial={"author": user})

    if req.method == "POST":
        form = CreateDiaryForm(req.POST, initial={"author": user})

        if form.is_valid():
            form.save()

            return redirect("/")

    return render(req, "diary/create.html", {"form": form, "user": req.user})
