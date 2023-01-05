from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView
from uweflixApp.forms import ClubForm, MonthlyStatementForm, UserAccountForm
from uweflixApp.models import Club, MonthlyStatement, UserAccount

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

def updateClub(request, pk):
    club = Club.objects.get(pk=pk)
    form = ClubForm(request.POST or None, instance=club)

    if request.method == "POST":
        if form.is_valid():
            club = form.save(commit=False)

            club.save()
            return redirect("home")
    else:
        return render(request, "uweflixApp/updateClub.html", {"form": form})

def deleteClub(request, pk):
    club = Club.objects.get(pk=pk)
    club.delete()
    return redirect("home")

def CreateMonthlyStatement(request):
    form = MonthlyStatementForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            statement = form.save(commit=False)

            statement.save()
            return redirect("home")
    else:
        return render(request, "uweflixApp/createMonthlyStatement.html", {"form": form})

def CreateUserAccount(request):
    form = UserAccountForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            user = form.save(commit=False)

            user.save()
            return redirect("home")
    else:
        return render(request, "uweflixApp/createUserAccount.html", {"form": form})





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

class UserAccountListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = UserAccount

    def get_context_data(self, **kwargs):
        context = super(UserAccountListView, self).get_context_data(**kwargs)
        return context