from django.shortcuts import render, redirect, get_object_or_404
from .forms import MemberForm
from django.template.loader import render_to_string 

# Create your views here.
from django.http import HttpResponse
# def homepage(request):
#     return HttpResponse("<h1>Bienvenue sur ma communaute des Polytechniciens</h1>")

from django.shortcuts import render, redirect
from django.contrib import messages  # ✅ Importer messages pour afficher les notifications
from .forms import MemberForm
from .models import Member  # ✅ Import Member model


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

def update_member(request, member_id):
    member = get_object_or_404(Member, id=member_id)  # ✅ Get the member by ID

    if request.method == "POST":
        form = MemberForm(request.POST, request.FILES, instance=member)  # ✅ Load existing data
        if form.is_valid():
            form.save()
            messages.success(request, f"{member.full_name} a été mis à jour avec succès !")
            return redirect("members_list")  # ✅ Redirect to list page
        else:
            messages.error(request, "Erreur lors de la mise à jour. Vérifiez votre formulaire.")
    else:
        form = MemberForm(instance=member)  # ✅ Pre-fill the form with existing data

    return render(request, "polytechnicien/update_member.html", {"form": form, "member": member})

def delete_member(request, member_id):
    member = get_object_or_404(Member, id=member_id)  # ✅ Get the member

    if request.method == "POST":
        member.delete()  # ✅ Delete from database
        messages.success(request, f"{member.full_name} a été supprimé avec succès !")
        return redirect("members_list")

    return render(request, "polytechnicien/delete_member.html", {"member": member})


def members_list(request):
    members = Member.objects.all()  # ✅ Fetch all members from the database
    return render(request, "polytechnicien/members_list.html", {"members": members})