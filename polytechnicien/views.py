from django.shortcuts import render
from .forms import MemberForm
from django.template.loader import render_to_string 

# Create your views here.
from django.http import HttpResponse
# def homepage(request):
#     return HttpResponse("<h1>Bienvenue sur ma communaute des Polytechniciens</h1>")

from django.shortcuts import render, redirect
from django.contrib import messages  # ✅ Importer messages pour afficher les notifications
from .forms import MemberForm

def homepage(request):
    if request.method == "POST":
        form = MemberForm(request.POST, request.FILES)  # ✅ Inclure les fichiers
        if form.is_valid():
            form.save()  # ✅ Enregistrer dans la base de données
            messages.success(request, "Merci pour ton inscription ! 🎉")  # ✅ Message de succès
            return redirect("homepage")  # ✅ Rediriger pour vider le formulaire après soumission
        else:
            messages.error(request, "Erreur lors de l'inscription. Vérifie ton formulaire.")  # ✅ Message d'erreur
    else:
        form = MemberForm()  # ✅ Formulaire vide par défaut

    return render(request, "polytechnicien/index.html", locals())


def member_view(request , member_id):
    return render(request, 'polytechnicien/member_view.html', locals())