from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from cmln.models.model_aerd import Aerd, Departement
from cmln.models.model_membre import Membre,Extension


#Register your models here.

class MembreAdmin(ImportExportModelAdmin):
    list_display = ('nom','prenom', 'email', 'get_adresse_complete_str', 'updated_at')

class AerdAdmin(ImportExportModelAdmin):
    list_display = ('nom','prenom', 'email', 'updated_at')

class ExtensionAdmin(ImportExportModelAdmin):
    list_display = ('nom', 'description', 'get_nom_description_str', 'pays')

class DepartementAdmin(ImportExportModelAdmin):
    list_display = ('nom','ministere')

admin.site.register(Membre, MembreAdmin)
admin.site.register(Aerd, AerdAdmin)
admin.site.register(Extension, ExtensionAdmin)
admin.site.register(Departement, DepartementAdmin)