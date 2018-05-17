from django.db import models

# Create your models here.

class PanelBoard(models.Model):

    types = (('B','Bi-phasic'),('T','Tri-phasic'))
    load_type = models.CharField(max_length = 1, choices = types)

    num_circuits = models.IntegerField()

'''
class Loads(models.Model):

    Num_cir = models.ForeignKey(panel_config, on_delete=models.SET_NULL, null=True)


def Num_of_loads(self):


    circuit_name = models.CharField(max_length=100)
    load = models.IntegerField()

    types = (('M', 'Mono-phasic'),('B','Bi-phasic'),('T','Tri-phasic'))
    load_type = models.CharField(max_length = 1, choices = types)

    load = models.IntegerField()

class PanelBoard(models.Model):

'''

