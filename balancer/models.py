from django.db import models

# Create your models here.

class Load(models.Model):

    types = (('M', 'Mono-phasic'),('B','Bi-phasic'),('T','Tri-phasic'))
    load_type = models.CharField(max_length = 1, choices = types)

    load = models.IntegerField()

class PanelBoard(models.Model):

    panel_types = (('M', 'Mono-phasic'),('B','Bi-phasic'),('T','Tri-phasic'))
    panel_type = models.CharField(max_length = 1, choices = panel_types)


