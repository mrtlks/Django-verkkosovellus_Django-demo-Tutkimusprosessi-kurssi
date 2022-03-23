from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

  
#https://docs.djangoproject.com/en/4.0/topics/forms/
#Koodi lomakkeen käsittelyyn 

def signup(request):
   
    # Jos tämä on POST -pyyntö (POST request), käsitellään lomakkeen data
    if request.method == 'POST':
        
        # luodaan lomakkeesta instanssi eli ilmentymä ja täytetään se pyynnön datalla:
        form = UserCreationForm(request.POST)
   
        # tarkistetaan onko lomake kelpoinen (valid)
        if form.is_valid():        

            # jos lomake on kelpoinen, data tallennetaan           
             form.save()

            # käyttäjä siirretään sivulle "home"
             return redirect('home')

    # jos pyyntö ei ole POST-pyyntö, luodaan tyhjä rekisteröitymislomake:
    else:
        form = UserCreationForm()

    # lomakkeen esittäminen
    return render(request, 'registration/signup.html', {
        'form': form
        })


@login_required # näkymät toimivat vain, jos käyttäjä on kirjautunut

def test_login_required(request):
    return render (request, 'test_login_required.html')

class test_login_required2(LoginRequiredMixin, TemplateView):
    template_name ='test_login_required.html'

