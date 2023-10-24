from django.contrib.auth.decorators import login_required
from django.db.models import Sum, F, Count
from django.db.models.functions import ExtractMonth, ExtractYear, \
    Extract  # ExtractMonth pour extraire le mois dans une date
from django.utils.translation import get_language, activate

from activite.models import Activite
from cmlnGestion.models.model_membre import Membre, Extension
from django.shortcuts import render
from django.utils import timezone

from cmlnGestion.models.model_aerd import Aerd
import calendar
import datetime
import locale


@login_required
def index(request):
    selected = "home"
    activites = Activite.objects.all()

    #extraire l'année
    locale.setlocale(locale.LC_TIME, 'fr_FR') # traduire le calendrier en Francais
    today = datetime.date.today()
    mois = today.month-1
    monthName = calendar.month_name[mois]
    year = Activite.objects.annotate(year=ExtractYear('date')).values('year').filter(year=today.year)
    month = Activite.objects.annotate(month=ExtractMonth('date')).values('month').filter(month=today.month)

    monthname =[]
    for d in month:
        monthname.append(calendar.month_name[d['month']])

    #============= DONNEES DES STATISQUES PAR MOIS =============

    # 1. FOR ALL
    activites_dash = Activite.objects.filter(date__year=today.year).annotate(month=ExtractMonth('date')).values('month').annotate(count=Sum(F('nbre_hommes') + F('nbre_femmes')+ F('nbre_enfants'))).values('month', 'count').order_by('month')
    monthNumber=[]
    totalParticipants = []
    for d in activites_dash:
        monthNumber.append(calendar.month_name[d['month']])
        totalParticipants.append(d['count'])

    # 2. FOR EXTENSION 1
    activites_dash1 = Activite.objects.filter(extension__id=1, date__year=today.year).annotate(month=ExtractMonth('date')).values(
        'month').annotate(count=Sum(F('nbre_hommes') + F('nbre_femmes') + F('nbre_enfants'))).values('month','count').order_by('month')
    monthNumber1 = []
    totalParticipants1 = []
    for d in activites_dash1:
        monthNumber1.append(calendar.month_name[d['month']])
        totalParticipants1.append(d['count'])

    # 2. FOR EXTENSION 1
    activites_dash2 = Activite.objects.filter(extension__id=2, date__year=today.year).annotate(
        month=ExtractMonth('date')).values(
        'month').annotate(count=Sum(F('nbre_hommes') + F('nbre_femmes') + F('nbre_enfants'))).values('month',
                                                                                                     'count').order_by(
        'month')
    monthNumber2 = []
    totalParticipants2 = []
    for d in activites_dash2:
        monthNumber2.append(calendar.month_name[d['month']])
        totalParticipants2.append(d['count'])



    # ==================== TOTAL DES MEMBRES ===================
    members_count = Membre.objects.all().count()
    #Pour l'extension n°1
    members_count_1 = Membre.objects.filter(extension__id=1).count()

    #Pour l'extension n°2
    members_count_2 = Membre.objects.filter(extension__id=2).count()

    # ==== Total des AERDs ====
    aerds_count = Aerd.objects.all().count()

    # Pour l'extension n°1
    aerds_count_1 = Aerd.objects.filter(extension__id=1).count()
    aerds_count_2 = Aerd.objects.filter(extension__id=2).count()

    # ==== Extension name ===
    extension = Extension.objects.all()



    # =========  NOUVEAUX VENUS =============

    # 1. Total des nouveaux venus extension confondus
    #nveaux_venus = Activite.objects.all().aggregate(Sum('nouveaux_venus'))['nouveaux_venus__sum'] or 0.00
    nveaux_venus = Activite.objects.filter(date__month=today.month -1).aggregate(Sum('nouveaux_venus'))['nouveaux_venus__sum'] or 0

    # 2. Total des nouveaux venus extension confondus
    nveaux_venus1 = Activite.objects.filter(extension__id=1, date__month=today.month -1).aggregate(Sum('nouveaux_venus'))['nouveaux_venus__sum'] or 0

    # 3. Total des nouveaux venus extension confondus
    nveaux_venus2 = Activite.objects.filter(extension__id=2, date__month=today.month -1).aggregate(Sum('nouveaux_venus'))[
                        'nouveaux_venus__sum'] or 0



    if aerds_count != 0:
        percentage = int((aerds_count / members_count) * 100)
    else:
        percentage = "0"

    if aerds_count_1 != 0:
        percentage1 = int((aerds_count_1 / members_count_1) * 100)
    else:
        percentage1 = "0"

    if aerds_count_2 != 0:
        percentage2 = int((aerds_count_2 / members_count_2) * 100)
    else:
        percentage2 = "0"


    context = {
        'today': today,

        'activites': activites,
        'activites_dash': activites_dash,

        'monthNumber': monthNumber,
        'monthNumber1': monthNumber1,
        'monthNumber2': monthNumber2,

        'totalParticipants': totalParticipants,
        'totalParticipants1': totalParticipants1,
        'totalParticipants2': totalParticipants2,

        'nveaux_venus': nveaux_venus,
        'nveaux_venus1': nveaux_venus1,
        'nveaux_venus2': nveaux_venus2,

        'year': year,
        'month': month,
        'monthName': monthName,
        'extension': extension,



        #MEMBRES
        'members_count': members_count,
        'members_count_1': members_count_1,
        'members_count_2': members_count_2,

        #AERDS
        'aerds_count': aerds_count,
        'aerds_count_1': aerds_count_1,
        'aerds_count_2': aerds_count_2,

        'percentage': percentage,
        'percentage1': percentage1,
        'percentage2': percentage2,

    }

    return render(request, "cmln/home.html", context)

def dashboard1(request):
    return render(request, "cmln/dashboard1.html")