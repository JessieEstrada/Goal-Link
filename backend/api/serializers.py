from rest_framework import serializers
from .models import CustomUser, Team, TeamMembership, Match

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id', 'username','password','first_name', 'last_name', 'email',
            'birth_month', 'birth_year', 'is_coach', 'current_team',
            'bio', 'achievements', 'positions_played'
        ]
        extra_kwargs = {"password": {"write_only": True}}
        
    def create(self, validated_data):
        password = validated_data.pop('password')  # Extract password
        user = CustomUser.objects.create_user(**validated_data)  # Use create_user() to hash the password
        user.set_password(password)  # Ensure password is hashed
        user.save()
        return user

class TeamSerializer(serializers.ModelSerializer):
    owner = CustomUserSerializer(read_only=True)
    members = CustomUserSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = [
            'id', 'name', 'owner', 'date_founded', 'members',
            'description', 'location', 'home_field', 'creation_date'
        ]

class TeamMembershipSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer(read_only=True)
    team = serializers.StringRelatedField()  # Use `team.name`

    class Meta:
        model = TeamMembership
        fields = ['id', 'team', 'user', 'role', 'joined_at']

class MatchSerializer(serializers.ModelSerializer):
    team1 = TeamSerializer(read_only=True)
    team2 = TeamSerializer(read_only=True)
    created_by = CustomUserSerializer(read_only=True)

    class Meta:
        model = Match
        fields = ['id', 'team1', 'team2', 'date', 'time', 'location', 'result', 'created_by']
