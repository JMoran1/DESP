from django.urls import path
from uweflixApp import views
from uweflixApp.models import Club, MonthlyStatement, UserAccount

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

user_list_view = views.UserAccountListView.as_view(
    queryset=UserAccount.objects.order_by("-userID")[:5],  # :5 limits the results to the five most recent
    context_object_name="user_list",
    template_name="uweflixApp/listUsers.html",
)

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("CreateClub/", views.createClub, name="CreateClub"),
    path("listClub/", club_list_view, name="listClub"),
    path("CreateMonthlyStatement/", views.CreateUserAccount, name="CreateMonthlyStatement"),
    path("ListMonthlyStatement/", user_list_view, name="ListMonthlyStatement"),
    path("updateClub/<int:pk>/", views.updateClub, name="updateClub"),
    path("deleteClub/<int:pk>/", views.deleteClub, name="deleteClub"),
]

