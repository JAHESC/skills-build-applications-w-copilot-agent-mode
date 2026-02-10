from djongo import models

class Team(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class User(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Activity(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.user.name} - {self.description}"

class Workout(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    reps = models.IntegerField()

    def __str__(self):
        return self.name

class Leaderboard(models.Model):
    _id = models.ObjectIdField(primary_key=True, editable=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()

    def __str__(self):
        return f"{self.team.name} - {self.points}"
