from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView

from cmlnGestion.forms.form_extension import ExtensionForm
from cmlnGestion.models.model_membre import Extension


@login_required()
def list_extension(request):
    extensions = Extension.objects.all()
    return render(request, "extensions/extensions.html", {"extensions":extensions})

class CreateExtension(CreateView, LoginRequiredMixin):
    model = Extension
    form_class = ExtensionForm
    template_name = "extensions/extension_form.html"

    def get_success_url(self):
        messages.success(self.request, "Extension ajouté avec succès")
        return reverse_lazy("extensions", kwargs={"pk":self.object.id})

# ============================ DETAILS AERD ========================================
class DetailExtension(DetailView, LoginRequiredMixin):
    model = Extension
    form_class = ExtensionForm
    template_name="extensions/extension_detail.html"

    """def get_departement(self, request):
        departement = Aerd.objects.all()
        if self.request.method == "POST":
            data = self.request.POST.getlist('')"""


# ============================ UPDATE AERD ========================================
class UpdateExtension(UpdateView, LoginRequiredMixin):
    model = Extension
    form_class = ExtensionForm
    template_name = "extensions/extension_form.html"

    def get_success_url(self):
        messages.success(self.request, "Extension modifié avec succès")
        return reverse_lazy("extensions", kwargs={"pk":self.object.id})

#====================== DELETE AERDS ========================
@login_required()
def delete_extension(request, id):
    pi = Extension.objects.get(pk=id)
    pi.delete()
    messages.success(request, "extension retiré avec succès")
    return redirect('extensions')
    # messages.success(request, "Item supprimé avec succès")