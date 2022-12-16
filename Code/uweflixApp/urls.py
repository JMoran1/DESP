from django.urls import path
from uweflixApp import views
from uweflixApp.models import Club, MonthlyStatement

club_list_view = views.ClubListView.as_view(
    queryset=Club.objects.order_by("-clubID")[:5],  # :5 limits the results to the five most recent
    context_object_name="club_list",
    template_name="uweflixApp/listClub.html",
)

statement_list_view = views.StatementListView.as_view(
    queryset=MonthlyStatement.objects.order_by("-statementID")[:5],  # :5 limits the results to the five most recent
    context_object_name="statement_list",
    template_name="uweflixApp/listStatements.html",
)

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("CreateClub/", views.createClub, name="CreateClub"),
    path("listClub/", club_list_view, name="listClub"),
    path("CreateMonthlyStatement/", views.CreateMonthlyStatement, name="CreateMonthlyStatement"),
    path("ListMonthlyStatement/", statement_list_view, name="ListMonthlyStatement"),
]

