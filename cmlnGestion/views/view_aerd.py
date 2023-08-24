from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView

from cmlnGestion.forms.form_aerd import AerdForm, AerdMinistereForm
from cmlnGestion.models.model_aerd import Aerd, AerdMinistere
from cmlnGestion.models.model_departement import Departement

# ============================ VIEW AERD ========================================
@login_required
def aerd_list(request):
    selected = "aerds"

    # Zone de recherche
    if 'q' in request.GET: # 'q' est le 'name' du search bar dans 'personne_list'
        q = request.GET['q']
        #personne_list = Personne.objects.filter(nom__icontains=q)
        multiple_q = Q(Q(departement__icontains=q) | Q(position__icontains=q))
        aerd_list = Aerd.objects.filter(multiple_q)

    else:
        aerd_list = Aerd.objects.all()

    # Pagination: 10 éléments par page
    paginator = Paginator(aerd_list.order_by('-updated_at'), 10)
    try:
        page = request.GET.get("page")
        if not page:
            page = 1
        aerd_list =paginator.page(page)
    except EmptyPage:
        #Si on dépasse la limite on prend la dernière page
        aerd_list = paginator.page(paginator.num_pages())

    aerd_ministeres= AerdMinistere.objects.all()

    return render(request, "cmln/aerd/aerd_list.html", locals())

# ============================ CREATE AERD ========================================

@login_required
def aerd_create(request):
    if request.method == 'POST':
        aerd_form = AerdForm(request.POST)
        ministere_form = AerdMinistereForm(request.POST)
        if aerd_form.is_valid and ministere_form.is_valid:
            aerd_form.save()
            ministere_form.save()
            return redirect("aerds")
    else:
        aerd_form = AerdForm()
        ministere_form = AerdMinistereForm()

    context = {
        "aerd_form": aerd_form,
        "ministere_form": ministere_form,
    }

    return render(request, "cmln/aerd/aerd_form.html", context)


class CreateAerd(CreateView, LoginRequiredMixin):
    model = Aerd
    form_class = AerdForm
    template_name = "cmln/aerd/aerd_form.html"

    def get_success_url(self):
        messages.success(self.request, "AERD ajouté avec succès")
        return reverse_lazy("detail_aerd", kwargs={"pk":self.object.id})

# ============================ DETAILS AERD ========================================
class DetailAerd(DetailView, LoginRequiredMixin):
    model = Aerd
    form_class = AerdForm
    template_name="cmln/aerd/aerd_detail.html"

    def get_departement(self, request):
        departement = Aerd.objects.all()
        if self.request.method == "POST":
            data = self.request.POST.getlist('')

# ============================ UPDATE AERD ========================================
class UpdateAerd(UpdateView, LoginRequiredMixin):
    model = Aerd
    form_class = AerdForm
    template_name = "cmln/aerd/aerd_form.html"

    def get_success_url(self):
        messages.success(self.request, "AERD modifié avec succès")
        return reverse_lazy("detail_aerd", kwargs={"pk":self.object.id})

#====================== DELETE AERDS ========================
@login_required()
def delete_aerd(request, id):
    pi = Aerd.objects.get(pk=id)
    pi.delete()
    messages.success(request, "AERD retiré avec succès")
    return redirect('aerds')
    # messages.success(request, "Item supprimé avec succès")



"""def aerd_create(request):
    if request.method == 'POST':
        form = AerdForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("aerds")
    else:
        form = AerdForm()

    context = {"form": form}

    return render(request, "cmln/aerd/aerd_form.html", locals(), context)"""


"""
"""