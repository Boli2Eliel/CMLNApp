from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from cmln.models.model_aerd import *
from cmln.models.model_membre import *


class MembreAdmin(ImportExportModelAdmin):
    list_display = ('nom','prenom', 'email', 'get_adresse_complete_str', 'updated_at')


class AerdAdmin(ImportExportModelAdmin):
    list_display = ('membre', 'position', 'situation', 'niveau_formation', 'responsabilite', 'extension',  'commentaire')


class ExtensionAdmin(ImportExportModelAdmin):
    list_display = ('nom', 'description', 'get_nom_description_str', 'pays')


class MinistereAdmin(ImportExportModelAdmin):
    list_display = ('designation', 'ministre', 'description')


class MinistreAdmin(ImportExportModelAdmin):
    list_display = ('aerd','date_entree', 'date_sortie', 'commentaire', )


class CoordonateurAdmin(ImportExportModelAdmin):
    list_display = ('aerd','date_entree', 'date_sortie', 'commentaire', )


class DepartementAdmin(ImportExportModelAdmin):
    list_display = ('designation','coordonateur', 'ministere', 'attributions', )


class ChargeAdmin(ImportExportModelAdmin):
    list_display = ('aerd','date_entree', 'date_sortie', 'commentaire', )


class OuvrierAdmin(ImportExportModelAdmin):
    list_display = ('aerd','date_entree', 'date_sortie', 'commentaire', )


class LeaderAdmin(ImportExportModelAdmin):
    list_display = ('aerd','principal', 'communaute', 'extension', 'date_entree', 'date_sortie', 'commentaire', )


class PasteurAdmin(ImportExportModelAdmin):
    list_display = ('aerd', 'extension', 'date_entree', 'date_sortie', 'commentaire', )


class AssistantPasteurAdmin(ImportExportModelAdmin):
    list_display = ('aerd', 'extension', 'stagiaire', 'pasteur', 'date_entree', 'date_sortie', 'commentaire', )

class AncienAdmin(ImportExportModelAdmin):
    list_display = ('aerd', 'extension', 'date_entree', 'date_sortie', 'commentaire', )


class DiacreAdmin(ImportExportModelAdmin):
    list_display = ('aerd', 'extension', 'date_entree', 'date_sortie', 'commentaire', )


admin.site.register(Membre, MembreAdmin)
admin.site.register(Aerd, AerdAdmin)
admin.site.register(Extension, ExtensionAdmin)
admin.site.register(Ministere, MinistereAdmin)
admin.site.register(Ministre, MinistreAdmin)
admin.site.register(Coordonateur, CoordonateurAdmin)
admin.site.register(Departement, DepartementAdmin)
admin.site.register(Charge, ChargeAdmin)
admin.site.register(Ouvrier, OuvrierAdmin)
admin.site.register(Leader, LeaderAdmin)
admin.site.register(Pasteur, PasteurAdmin)
admin.site.register(AssistantPasteur, AssistantPasteurAdmin)
admin.site.register(Ancien, AncienAdmin)
admin.site.register(Diacre, DiacreAdmin)
