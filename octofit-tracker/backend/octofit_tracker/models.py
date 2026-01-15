from django.db import models

# Utilisateur
class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    team = models.ForeignKey('Team', null=True, blank=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.username

# Équipe
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    members = models.ManyToManyField(User, related_name='teams', blank=True)
    def __str__(self):
        return self.name

# Activité
class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()  # minutes
    date = models.DateField()
    def __str__(self):
        return f"{self.type} - {self.user.username}"

# Workout personnalisé
class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    def __str__(self):
        return f"{self.name} - {self.user.username}"

# Leaderboard
class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.team.name} - {self.points} pts"
