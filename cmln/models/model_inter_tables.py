from django_countries.fields import CountryField
from django.db import models
from enum import Enum
from cmln.models.model_membre import *
from cmln.models.model_aerd import *




class MembreAerd(models.Model):
    membre = models.ForeignKey(Membre, on_delete=models.CASCADE, null=True, blank=True)
    aerd = models.ForeignKey(Aerd, on_delete=models.CASCADE, null=True, blank=True)


class AerdPosition(models.Model):
    aerd = models.ForeignKey(Aerd, on_delete=models.CASCADE, null=True, blank=True)
    leader = models.ForeignKey(Leader, on_delete=models.CASCADE, null=True, blank=True)
    pasteur = models.ForeignKey(Pasteur, on_delete=models.CASCADE, null=True, blank=True)
    assistant_pasteur = models.ForeignKey(AssistantPasteur, on_delete=models.CASCADE, null=True, blank=True)
    ancien = models.ForeignKey(Ancien, on_delete=models.CASCADE, null=True, blank=True)
    diacre = models.ForeignKey(Diacre, on_delete=models.CASCADE, null=True, blank=True)



