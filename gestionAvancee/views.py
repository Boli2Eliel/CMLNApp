from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView

from cmlnGestion.models.model_aerd import Ministere
from gestionAvancee.forms import ExtensionForm, MinistereForm
from gestionAvancee.models import Extension


# ######################################## EXTENSIONS #################################################
@login_required()
def list_extension(request):
    extensions = Extension.objects.all()
    return render(request, "extensions/extensions.html", {"extensions": extensions})


# ============================ CREATE EXTENSION ========================================
class CreateExtension(CreateView, LoginRequiredMixin):
    model = Extension
    form_class = ExtensionForm
    template_name = "extensions/extension_form.html"

    def get_success_url(self):
        messages.success(self.request, "Extension ajouté avec succès")
        return reverse_lazy("extensions", kwargs={"pk": self.object.id})


# ============================ DETAILS EXTENSION ========================================
class DetailExtension(DetailView, LoginRequiredMixin):
    model = Extension
    form_class = ExtensionForm
    template_name = "extensions/extension_detail.html"

    """def get_departement(self, request):
        departement = Aerd.objects.all()
        if self.request.method == "POST":
            data = self.request.POST.getlist('')"""


# ============================ UPDATE EXTENSION ========================================
class UpdateExtension(UpdateView, LoginRequiredMixin):
    model = Extension
    form_class = ExtensionForm
    template_name = "extensions/extension_form.html"

    def get_success_url(self):
        messages.success(self.request, "Extension modifié avec succès")
        return reverse_lazy("extensions", kwargs={"pk": self.object.id})


# ====================== DELETE EXTENSION ========================
@login_required()
def delete_extension(request, id):
    pi = Extension.objects.get(pk=id)
    pi.delete()
    messages.success(request, "extension retiré avec succès")
    return redirect('extensions')
    # messages.success(request, "Item supprimé avec succès")



# ######################################## MIINISTERES #################################################
@login_required()
def list_ministeres(request):
    ministeres = Ministere.objects.all()
    return render(request, "ministeres/ministeres.html", {"ministeres": ministeres})


# ============================ CREATE EXTENSION ========================================
class CreateMinistere(CreateView, LoginRequiredMixin):
    model = Ministere
    form_class = MinistereForm
    template_name = "ministeres/ministere_form.html"

    def get_success_url(self):
        messages.success(self.request, "Ministère ajouté avec succès")
        return reverse_lazy("ministeres", kwargs={"pk": self.object.id})


# ============================ DETAILS EXTENSION ========================================
class DetailMinistere(DetailView, LoginRequiredMixin):
    model = Ministere
    form_class = MinistereForm
    template_name = "ministeres/ministere_detail.html"

    """def get_departement(self, request):
        departement = Aerd.objects.all()
        if self.request.method == "POST":
            data = self.request.POST.getlist('')"""


# ============================ UPDATE EXTENSION ========================================
class UpdateMinistere(UpdateView, LoginRequiredMixin):
    model = Ministere
    form_class = MinistereForm
    template_name = "ministeres/ministere_form.html"

    def get_success_url(self):
        messages.success(self.request, "Ministère modifié avec succès")
        return reverse_lazy("ministeres", kwargs={"pk": self.object.id})


# ====================== DELETE EXTENSION ========================
@login_required()
def delete_ministere(request, id):
    pi = Extension.objects.get(pk=id)
    pi.delete()
    messages.success(request, "Ministere retiré avec succès")
    return redirect('ministeres')
    # messages.success(request, "Item supprimé avec succès")
