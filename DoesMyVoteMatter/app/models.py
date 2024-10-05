from django.db import models

PARTY = [
    ('R', 'Republican'),
    ('D', 'Democratic')
]

from django.db import models

class State(models.Model):
    name = models.CharField(max_length=100, unique=True)
    abbreviation = models.CharField(max_length=2, unique=True)

    def __str__(self):
        return self.name

class District(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    district = models.IntegerField() 
    area = models.IntegerField()
    perimeter = models.IntegerField()
    congress = models.IntegerField()
    party = models.CharField(max_length=1, default="", choices=PARTY)
    
    def district_name(self):
        return self.name
