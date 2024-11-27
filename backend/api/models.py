from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Overriding first_name, last_name, and email
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)  
    email = models.EmailField(unique=True, blank=False)   
    # Additional custom fields 
    birth_month = models.IntegerField(choices=[(i, i) for i in range(1, 13)], null=True, blank=True)
    birth_year = models.IntegerField(null=True, blank=True)
    is_coach = models.BooleanField(default=False)
    current_team = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    achievements = models.TextField(blank=True)
    positions_played = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.username
    
class Team(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='owned_teams')  
    date_founded = models.DateField(null=True, blank=True)
    members = models.ManyToManyField(CustomUser, related_name='teams')
    creation_date = models.DateTimeField(auto_now_add=True)  

    def save(self, *args, **kwargs):
        if not self.date_founded:
            self.date_founded = self.creation_date.date()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class TeamMembership(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=[('player', 'Player'), ('captain', 'Captain')], default='player')
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.team.name} ({self.role})"