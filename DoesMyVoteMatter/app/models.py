from django.db import models

PARTY = [
    ('R', 'Republican'),
    ('D', 'Democratic')
]

class District(models.Model):
    name = models.CharField(max_length=255)
    district = models.IntegerField() 
    area = models.IntegerField()
    perimeter = models.IntegerField()
    congress = models.IntegerField()
    party = models.CharField(max_length=1, default="", choices=PARTY)
    
    def district_name(self):
        return self.name