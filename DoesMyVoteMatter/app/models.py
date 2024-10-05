from django.db import models

class district(models.Model):
    name = models.CharField(max_length=255)

    def district_name(self):
        return self.district.name