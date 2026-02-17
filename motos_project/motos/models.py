from django.db import models

class Fabricant(models.Model):
    nom = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Pilot(models.Model):
    nom = models.CharField(max_length=100)
    nacionalitat = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Moto(models.Model):
    model = models.CharField(max_length=100)
    any = models.IntegerField()
    fabricant = models.ForeignKey(Fabricant, on_delete=models.CASCADE)
    pilots = models.ManyToManyField(Pilot)

    def __str__(self):
        return self.model

