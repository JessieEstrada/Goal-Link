from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_coach = models.BooleanField(default=False)
    bio = models.TextField(blank=True)
    stats = models.JSONField(default=dict, blank=True)
    team_role = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.username
    
class Team(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='owned_teams')
    members = models.ManyToManyField(CustomUser, related_name='teams')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class TeamMembership(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=[('player', 'Player'), ('captain', 'Captain')], default='player')
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.team.name} ({self.role})"
