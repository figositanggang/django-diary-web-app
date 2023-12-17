from django.shortcuts import redirect, render

from .forms import CreateDiaryForm
from .models import Diary


# Create your views here.
def index(req):
    diaries = Diary.objects.order_by("-created_at")

    return render(req, "diary/index.html", {"diaries": diaries})


def create(req):
    form = CreateDiaryForm

    if req.method == "POST":
        form = CreateDiaryForm(req.POST, instance=req.user)

        if form.is_valid():
            form.save()

            return redirect("/")

    return render(req, "diary/create.html", {"form": form, "user": req.user})
