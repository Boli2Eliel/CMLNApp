from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from cmln.forms.form_aerd import AerdForm
from cmln.models.model_aerd import Aerd


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

    return render(request, "cmln/aerd/aerd_list.html", locals())

class CreateAerd(CreateView, LoginRequiredMixin):
    model = Aerd
    form_class = AerdForm
    template_name = "cmln/aerd/aerd_form.html"

    def get_success_url(self):
        return reverse_lazy("detail_aerd", kwargs={"pk":self.object.id})

class UpdateAerd(UpdateView, LoginRequiredMixin):
    model = Aerd
    form_class = AerdForm
    template_name = "cmln/aerd/aerd_form.html"

    def get_success_url(self):
        return reverse_lazy("detail_aerd", kwargs={"pk":self.object.id})


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