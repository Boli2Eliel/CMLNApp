from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.http import urlencode
from django.views.generic import CreateView, UpdateView

from cmln.forms.form_personne import MembreForm
from cmln.models.model_membre import *
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

    """if request.method == "POST":
        form = PersonneSearchForm(request.POST)
        if form.is_valid():
            base_url = reverse('personnes')
            query_string = urlencode(form.cleaned_data)
            url = '{}?{}'.format(base_url, query_string)
            return redirect(url)
    else:
        form = PersonneSearchForm()
        nom_form = request.GET.get("nom", "")
        prenom_form = request.GET.get("prenom", "")
        email_form = request.GET.get("email", "")

        if nom_form is not None:
            personne_list = personne_list.filter(nom__icontains=nom_form)
            form.fields['nom'].initial = nom_form

        if prenom_form is not None:
            personne_list = personne_list.filter(prenom__icontains=prenom_form)
            form.fields['prenom'].initial = prenom_form

        if email_form is not None:
            personne_list = personne_list.filter(email__icontains=email_form)
            form.fields['email'].initial = email_form"""

    # Pagination: 10 éléments par page
    paginator = Paginator(membre_list.order_by('-updated_at'), 10)
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
        return reverse_lazy("detail_membre", kwargs={"pk":self.object.id})


class UpdateMembre(UpdateView,LoginRequiredMixin):
    model = Membre
    form_class = MembreForm
    template_name = "cmln/membre/membre_form.html"

    def get_success_url(self):
        return reverse_lazy("detail_membre", kwargs={"pk": self.object.id})
