from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import CustomUser, Team, TeamMembership, Match
from .serializers import CustomUserSerializer, TeamSerializer, TeamMembershipSerializer, MatchSerializer


# Create your views here.
class CreateCustomUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny] # Allow any user to register

# Retrieve User Details (User can only view their own data)
class RetrieveCustomUserView(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Ensure users can only access their own data
        return self.request.user

# Update User Profile (Only the authenticated user can update their profile)
class UpdateCustomUserView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Ensure users can only update their own profile
        return self.request.user

# Delete User (Only the user themselves or an admin can delete)
class DeleteCustomUserView(generics.DestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        # Ensure users can only delete their own profile
        return self.request.user