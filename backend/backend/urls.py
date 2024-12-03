from django.contrib import admin
from django.urls import path, include
from api.views import (
    CreateCustomUserView,
    RetrieveCustomUserView,
    UpdateCustomUserView,
    DeleteCustomUserView
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),
    
    # User-related endpoints
    path("api/user/register/", CreateCustomUserView.as_view(), name="register"),
    path("api/user/<int:pk>/", RetrieveCustomUserView.as_view(), name="retrieve_user"),  # View own profile or by admin
    path("api/user/<int:pk>/update/", UpdateCustomUserView.as_view(), name="update_user"),  # Update own profile
    path("api/user/<int:pk>/delete/", DeleteCustomUserView.as_view(), name="delete_user"),  # Delete own account
    
    # Token-based authentication
    path("api/token/", TokenObtainPairView.as_view(), name="get_token"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("api-auth/", include("rest_framework.urls")),
]
