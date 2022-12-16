from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView
from uweflixApp.forms import ClubForm, MonthlyStatementForm
from uweflixApp.models import Club, MonthlyStatement

# Create your views here.

def home(request):
    return render(request, "uweflixApp/index.html")

def about(request):
    return render(request, "uweflixApp/base.html")

def contact(request):
    return render(request, "uweflixApp/base.html")

def createClub(request):
    form = ClubForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            club = form.save(commit=False)

            club.save()
            return redirect("home")
    else:
        return render(request, "uweflixApp/createClub.html", {"form": form})

def CreateMonthlyStatement(request):
    form = MonthlyStatementForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            statement = form.save(commit=False)

            statement.save()
            return redirect("home")
    else:
        return render(request, "uweflixApp/createMonthlyStatement.html", {"form": form})



class ClubListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = Club

    def get_context_data(self, **kwargs):
        context = super(ClubListView, self).get_context_data(**kwargs)
        return context

class StatementListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = MonthlyStatement

    def get_context_data(self, **kwargs):
        context = super(StatementListView, self).get_context_data(**kwargs)
        return context