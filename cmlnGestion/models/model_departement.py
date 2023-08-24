from django.db import models

class Departement(models.Model):
    designation = models.CharField( max_length=100, blank=True, null=True, verbose_name="Nom")
    attributions = models.CharField(max_length=300, blank=True, null=True, verbose_name="Attributions", )
    def __str__(self):
        return self.designation
