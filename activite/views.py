from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView

from activite.models import Activite
from activite.forms import ActiviteForm
from cmlnGestion.models.model_aerd import Aerd
from cmlnGestion.models.model_departement import Departement
import datetime


def activite(request):

    selected = "activites"

    # Zone de recherche
    if 'q' in request.GET:  # 'q' est le 'name' du search bar dans 'personne_list'
        q = request.GET['q']
        # personne_list = Personne.objects.filter(nom__icontains=q)
        multiple_q = Q(Q(type__icontains=q) | Q(extension__icontains=q))
        activite_list = Activite.objects.filter(multiple_q)

    else:
        activite_list = Activite.objects.all()

    # Pagination: 10 éléments par page
    paginator = Paginator(activite_list.order_by('-date'), 10)
    try:
        page = request.GET.get("page")
        if not page:
            page = 1
        activite_list = paginator.page(page)
    except EmptyPage:
        # Si on dépasse la limite on prend la dernière page
        activite_list = paginator.page(paginator.num_pages())

    return render(request, "activites/activite.html", locals())


class CreateActivite(CreateView, LoginRequiredMixin):
    model = Activite
    form_class = ActiviteForm
    template_name = "activites/activite_form.html"

    def get_success_url(self):
        messages.success(self.request, "Activité ajouté avec succès")
        return reverse_lazy("detail_activite", kwargs={"pk":self.object.id})



class DetailActivite(DetailView, LoginRequiredMixin):
    model = Activite
    form_class = ActiviteForm
    template_name="activites/activite_detail.html"

    """def get_departement(self, request):
        departement = Activite.objects.all()
        if self.request.method == "POST":
            data = self.request.POST.getlist('')"""

class UpdateActivite(UpdateView, LoginRequiredMixin):
    model = Activite
    form_class = ActiviteForm
    template_name = "activites/activite_form.html"

    def get_success_url(self):
        messages.success(self.request, "Activité modifié avec succès")
        return reverse_lazy("detail_activite", kwargs={"pk":self.object.id})



#====================== DELETE ITEMS ========================

@login_required()
def delete_activite(request, id):
    pi = Activite.objects.get(pk=id)
    pi.delete()
    messages.success(request, "Activité retiré avec succès")
    return redirect('activites')
    # messages.success(request, "Item supprimé avec succès")

