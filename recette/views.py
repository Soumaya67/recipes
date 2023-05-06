from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from recette.forms import LoginForm, RecetteForm
from recette.models import Recette


@login_required
def dashboard(request):
    return render(request, 'registration/dashboard.html')

def home(request):
    return render(request, 'home.html')

def faqs(request):
    return render(request, 'faqs.html')

def ourteam(request):
    return render(request, 'OurTeam.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def contactus(request):
    return render(request, 'contactus.html')

def SignupPage(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(username,email,pass1)
            my_user.save()
            return redirect('login')
    return render(request, 'registration/signup.html')

def recette_list(request):
    recettes = Recette.objects.all()
    return render(request, 'Recipes.html', {'recettes': recettes})

def create_recette(request):
    if request.method == 'POST':
        form = RecetteForm(request.POST)  # if the user submit the form
        if form.is_valid():
            form.save()
            return redirect('recettes')
    else:
        form = RecetteForm()
        return render(request, 'create_recette.html', {'form': form})


def update_Recette(request, pk):
    recette = get_object_or_404(Recette, pk=pk)
    if request.method == 'POST':
        form = RecetteForm(request.POST, instance=recette)
        if form.is_valid():
            form.save()
            return redirect('recettes')
    else:
        form = RecetteForm(instance=recette)
        return render(request, 'update_recette.html', {'form': form, 'patient': recette})


def delete_patient(request, pk):
    patient = get_object_or_404(Recette, pk=pk)
    patient.delete()
    return redirect('recettes')


def search(request):
    query = request.GET.get('keyword')
    recettes = Recette.objects.filter(nom__contains=query)
    return render(request, 'recettes.html', {'recettes': recettes})




