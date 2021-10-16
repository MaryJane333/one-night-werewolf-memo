from django.db import models

# Create your models here.
class NameModel(models.Model):
    username = models.CharField(max_length=50, default="")
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class NumberModel(models.Model):
    villager = models.IntegerField(null=True, blank=True, default=0)
    fortune_teller = models.IntegerField(null=True, blank=True, default=0)
    thief = models.IntegerField(null=True, blank=True, default=0)
    werewolf = models.IntegerField(null=True, blank=True, default=0)
    madman = models.IntegerField(null=True, blank=True, default=0)
    username = models.CharField(max_length=50)