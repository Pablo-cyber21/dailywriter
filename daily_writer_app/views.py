from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect, Http404


# from django.urlresolvers import reverse
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required


from .models import Entry
from .forms import EntryForm


@login_required(login_url="/login")
def index(request):
    """The homepage of daily writer.com"""
    entries = Entry.objects.all()
    entries = Entry.objects.filter(author=request.user).order_by("date_added")
    return render(request, "daily_writer_app/index.html", {"entries": entries})


@login_required(login_url="/login")
def new_entry(request):
    """Add a new entry"""

    if request.method != "POST":
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.author = request.user
            new_entry.Entry = Entry
            new_entry.save()
            return redirect("/index")

    context = {"form": form}
    return render(request, "daily_writer_app/new_entry.html", context)


def edit_entry(request, entry_id):
    """To edit and existing entry"""
    entry = Entry.objects.get(id=entry_id)
    if entry.author != request.user:
        raise Http404

    if request.method != "POST":
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("/index")

    context = {"entry": entry, "form": form}
    return render(request, "daily_writer_app/edit_entry.html", context)


def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("/index")

    else:
        form = RegisterForm()

    return render(request, "registration/sign_up.html", {"form": form})
