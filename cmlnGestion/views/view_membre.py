
from dal import autocomplete
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.http import urlencode
from django.views.generic import CreateView, UpdateView

from cmlnGestion.forms.form_personne import MembreForm
from cmlnGestion.models.model_membre import *
from django.db.models import Q

@login_required
def membre_list(request):
    selected = "membres"

    # Zone de recherche
    if 'q' in request.GET: # 'q' est le 'name' du search bar dans 'membre_list'
        q = request.GET['q']
        #membre_list = Membre.objects.filter(nom__icontains=q)
        multiple_q = Q(Q(nom__icontains=q) | Q(prenom__icontains=q) | Q(ville__icontains=q))
        membre_list = Membre.objects.filter(multiple_q)

    else:
        membre_list = Membre.objects.all()

    # Pagination: 10 éléments par page
    paginator = Paginator(membre_list.order_by('-updated_at'), 6)
    try:
        page = request.GET.get("page")
        if not page:
            page = 1
        membre_list =paginator.page(page)
    except EmptyPage:
        #Si on dépasse la limite on prend la dernière page
        membre_list = paginator.page(paginator.num_pages())

    return render(request, "cmln/membre/membre_list.html", locals())


class CreateMembre(CreateView, LoginRequiredMixin):
    model = Membre
    form_class = MembreForm
    template_name = "cmln/membre/membre_form.html"

    def get_success_url(self):
        messages.success(self.request, "MEMBRE ajouté avec succès")
        return reverse_lazy("detail_membre", kwargs={"pk":self.object.id})

@login_required
def createMembre(request):
    submitted = False
    if request.method == 'POST':
        form = MembreForm(request.POST)
        if form.is_valid():
            #membre = form.save(commit=False)
            #membre.nom = request.user.id
            #membre.save()
            form.save()
            return reverse_lazy("detail_membre", kwargs={"pk": request.object.id})
    else:
        form = MembreForm()
        if 'submitted'in request.GET:
            submitted = True

    return render(request, "cmln/membre/membre_form.html", locals(),)


class UpdateMembre(UpdateView,LoginRequiredMixin):
    model = Membre
    form_class = MembreForm
    template_name = "cmln/membre/membre_form.html"

    def get_success_url(self):
        messages.success(self.request, "MEMBRE modifié avec succès")
        return reverse_lazy("detail_membre", kwargs={"pk": self.object.id})

@login_required()
def delete_membre(request, id):
    pi = Membre.objects.get(pk=id)
    pi.delete()
    messages.success(request, "Membre retiré avec succès")
    return redirect('membres')
    # messages.success(request, "Item supprimé avec succès")


class MembreAutocomplete(autocomplete.Select2QuerySetView): #A jouter au formulaire " form_aerd"
    def get_queryset(self):
        #Don't forget to filter out results dependig on the visitor!
        if not self.request.user.is_authenticated:
            return Membre.objects.none()

        qs = Membre.objects.all()
        if self.q:
            qs = qs.filter(nom__istartswith=self.q)

        return qs













""""""










"""def createMembre1(request):
    membre = Membre.objects.all()

    nom = request.POST.get('nom')
    prenom = request.POST.get('prenom')
    sexe = request.POST.get('sexe')
    date_naissance = request.POST.get('date_naissance')
    date_arrivee = request.POST.get('date_arrivee')
    baptise = request.POST.get('baptise')
    date_bapteme = request.POST.get('date_bapteme')
    situation = request.POST.get('situation')
    email = request.POST.get('email')
    adresse = request.POST.get('adresse')
    ville = request.POST.get('ville')
    extension = request.POST.get('extension')
    telephone = request.POST.get('telephone')
    commentaire = request.POST.get('commentaire')
    
    new_membre = Membre.objects.create(nom=nom, prenom=prenom, sexe=sexe, date_naissance=date_naissance, date_arrivee=date_arrivee, baptise=baptise, date_bapteme=date_bapteme, situation=situation, email=email, adresse=adresse, ville=ville, extension=extension, telephone= telephone, commentaire=commentaire )
    
    new_membre.save()

    return render(request, "cmlnGestion/membre/membre_create.html", locals(),)"""