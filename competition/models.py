from django.db import models
from django.conf import settings

# class User():
#     date_joined = "Date"
#     email = "Email"       <-
#     first_name = "Char"   <-
#     is_active = "Bool"
#     is_staff = "Bool"     <-
#     is_superuser = "Bool"
#     last_login = "Date"
#     last_name = "Char"
#     password = "Char"
#     username = "Char"

class Player(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    
    def __str__(self):
        return f"{self.name} ({self.user.username})"

class Competition(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(blank=True, null=True, max_length=100)
    organiser = models.ForeignKey(Player, on_delete=models.CASCADE)
    date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.organiser.name})"

class Satay(models.Model):
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
    cook = models.ForeignKey(Player, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cook.name} ({self.competition.name})"

class Rating(models.Model):
    satay = models.ForeignKey(Satay, on_delete=models.CASCADE)
    rater = models.ForeignKey(Player, on_delete=models.CASCADE)
    taste = models.IntegerField()  
    tenderness = models.IntegerField()  

    def __str__(self):
        return f"{self.rater.name} {self.taste}/{self.tenderness} (saté {self.satay.cook.name})"
