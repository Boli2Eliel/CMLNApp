from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from django.shortcuts import render

from cmln.models.model_aerd import Aerd


@login_required
def aerd_list(request):
    selected = "aerds"

    # Zone de recherche
    if 'q' in request.GET: # 'q' est le 'name' du search bar dans 'personne_list'
        q = request.GET['q']
        #personne_list = Personne.objects.filter(nom__icontains=q)
        multiple_q = Q(Q(nom__icontains=q) | Q(prenom__icontains=q) | Q(ville__icontains=q))
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
