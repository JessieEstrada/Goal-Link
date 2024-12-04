from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import CustomUser, Team, TeamMembership, Match
from .serializers import CustomUserSerializer, TeamSerializer, TeamMembershipSerializer, MatchSerializer
from rest_framework.exceptions import PermissionDenied

# CUSTOMER VIEWS

# Create User
class CreateCustomUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny] # Allow any user to register

# List Users (Only admins can list all users)
class ListCustomUserView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

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
    


# TEAM VIEWS
class CreateTeamView(generics.CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create a team

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)  # Automatically set the current user as the owner

class ListTeamView(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [AllowAny]  # ANY user can see teams

class RetrieveTeamView(generics.RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can retrieve teams

class UpdateTeamView(generics.UpdateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        team = self.get_object()
        if self.request.user != team.owner:
            raise PermissionDenied("You are not the owner of this team.")
        serializer.save()

class DeleteTeamView(generics.DestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        if self.request.user != instance.owner:
            raise PermissionDenied("You are not the owner of this team.")
        instance.delete()