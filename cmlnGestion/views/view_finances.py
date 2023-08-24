from django.contrib.auth.decorators import login_required
from django.db.models import Sum, F, Count
from django.db.models.functions import ExtractMonth, ExtractYear, \
    Extract  # ExtractMonth pour extraire le mois dans une date
from django.utils.translation import get_language, activate
from cmlnGestion.models.model_membre import Membre, Extension
from django.shortcuts import render
from django.utils import timezone

from cmlnGestion.models.model_aerd import Activite, Aerd
import calendar
import datetime
import locale

def dons_list(request):
    activites = Activite.objects.all()

    # extraire l'année
    locale.setlocale(locale.LC_TIME, 'fr_FR')  # traduire le calendrier en Francais
    today = datetime.date.today()
    mois = today.month
    monthName = calendar.month_name[mois]
    year = Activite.objects.annotate(year=ExtractYear('date')).values('year').filter(year=today.year)
    month = Activite.objects.annotate(month=ExtractMonth('date')).values('month').filter(month=today.month)

    context = {
        'activites': activites,
        'monthName': monthName,
    }

    return render(request, "finances/dons_list.html", context)