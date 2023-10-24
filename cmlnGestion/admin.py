from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from activite.models import Activite
from cmlnGestion.models.model_aerd import *
from cmlnGestion.models.model_departement import *
from cmlnGestion.models.model_membre import *


class MembreAdmin(ImportExportModelAdmin):
    list_display = ('nom','prenom', 'email', 'get_adresse_complete_str', 'updated_at')


class AerdAdmin(ImportExportModelAdmin):
    list_display = ('membre', 'position', 'situation', 'niveau_formation', 'responsabilite', 'extension',  'commentaire')


class ExtensionAdmin(ImportExportModelAdmin):
    list_display = ('id','nom', 'description', 'get_nom_description_str', 'pays')


class MinistereAdmin(ImportExportModelAdmin):
    list_display = ('designation', 'ministre', 'description')


class MinistreAdmin(ImportExportModelAdmin):
    list_display = ('id','coordonateur','date_entree', 'date_sortie', 'commentaire', )


class CoordonateurAdmin(ImportExportModelAdmin):
    list_display = ('id','aerd','date_entree', 'date_sortie', 'commentaire', )


class DepartementAdmin(ImportExportModelAdmin):
    list_display = ('designation', 'attributions', )


class ChargeAdmin(ImportExportModelAdmin):
    list_display = ('aerd','date_entree', 'date_sortie', 'commentaire', )


#class OuvrierAdmin(ImportExportModelAdmin):
    #list_display = ('aerd','date_entree', 'date_sortie', 'commentaire', )


class LeaderAdmin(ImportExportModelAdmin):
    list_display = ('pasteur','principal', 'communaute', 'extension', 'date_entree', 'date_sortie', 'commentaire', )


class PasteurAdmin(ImportExportModelAdmin):
    list_display = ('ministre', 'extension', 'date_entree', 'date_sortie', 'commentaire', )


class AssistantPasteurAdmin(ImportExportModelAdmin):
    list_display = ('coordonateur', 'extension', 'stagiaire', 'pasteur', 'date_entree', 'date_sortie', 'commentaire', )

class AncienAdmin(ImportExportModelAdmin):
    list_display = ('coordonateur', 'extension', 'date_entree', 'date_sortie', 'commentaire', )


class DiacreAdmin(ImportExportModelAdmin):
    list_display = ('charge', 'extension', 'date_entree', 'date_sortie', 'commentaire', )

class ActiviteAdmin(ImportExportModelAdmin):
    list_display = ('type', 'extension','date', 'heure_debut', 'heure_fin', 'theme', 'moderateur', 'intervenant', 'ref_biblique', 'resume', 'total_participants', 'total_offrandes' )


admin.site.register(Membre, MembreAdmin)
admin.site.register(Aerd, AerdAdmin)
admin.site.register(Extension, ExtensionAdmin)
admin.site.register(Ministere, MinistereAdmin)
admin.site.register(Ministre, MinistreAdmin)
admin.site.register(Coordonateur, CoordonateurAdmin)
admin.site.register(Departement, DepartementAdmin)
admin.site.register(Charge, ChargeAdmin)
admin.site.register(Leader, LeaderAdmin)
admin.site.register(Pasteur, PasteurAdmin)
admin.site.register(AssistantPasteur, AssistantPasteurAdmin)
admin.site.register(Ancien, AncienAdmin)
admin.site.register(Diacre, DiacreAdmin)
admin.site.register(Activite, ActiviteAdmin)
