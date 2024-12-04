from django.urls import path
from . import views

urlpatterns = [
    # User URLs
    path("user/list/", views.CreateCustomUserView.as_view(), name="list_users"),
    path("user/<int:pk>/", views.RetrieveCustomUserView.as_view(), name="retrieve_user"),  # View own profile or by admin
    path("user/<int:pk>/update/", views.UpdateCustomUserView.as_view(), name="update_user"),  # Update own profile
    path("user/<int:pk>/delete/", views.DeleteCustomUserView.as_view(), name="delete_user"),  # Delete own account
    
    # Team URLs
    path("teams/", views.ListTeamView.as_view(), name="list_teams"),
    path("teams/create/", views.CreateTeamView.as_view(), name="create_team"),
    path("teams/<int:pk>/", views.RetrieveTeamView.as_view(), name="retrieve_team"),
    path("teams/<int:pk>/update/", views.UpdateTeamView.as_view(), name="update_team"),
    path("teams/<int:pk>/delete/", views.DeleteTeamView.as_view(), name="delete_team"),

]