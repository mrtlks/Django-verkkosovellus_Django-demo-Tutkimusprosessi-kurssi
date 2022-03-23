
from django.shortcuts import render, redirect  
from example_project.app2.forms import ExampleForm  
from example_project.app2.models import Example  


# Djangossa ei voi olla yhtä useampaa näkymää samassa urlissa, joten kaikki urlin toiminnallisuudet
# on laitettava samaan näkymään. Näin ollen "home" -näkymä esittää listan olioista sekä myös
# tallentaa uuden olion listalle, jos kyseessä on POST-pyyntö.

# 1. Kotisivu
def home(request):

# 1 b. Lisätään uusi esimerkkiolio listalle, jos kyseessä on POST-pyyntö:
    if request.method == "POST":  
        form = ExampleForm(request.POST)  
        if form.is_valid():  
            form.save()  

        #uudelleenohjaaminen estää tietokannan päivittymisen uudelleen samoilla tiedoilla kuin edellinen tallennus.
        return redirect("/")  
        
# 1 a. jos home.html sivu vain ladataan (sivu ladataan aina ennen kuin 
# uuden olion lisäämiskaavaketta voi täyttää), haetaan kaikki esimerkkioliot listalle sekä myös esimerkkiolioiden 
# tallennuskaavake (ExampleForm) näkyville home.htm-sivulle.
    else:  
        form = ExampleForm()  

    examples = Example.objects.all()  

    # https://docs.djangoproject.com/en/2.1/ref/templates/api/#django.template.Context
    context = {'form': form, 'examples':examples}

    return render(request, 'home.html', context)
    


# 2. Näytetään kaikki listalla olevat esimerkkioliot (tätä näkymää voidaan käyttää, jos halutaan esittää lista omalla sivullaan):
def show(request):  
    examples = Example.objects.all()  
    return render(request,'crud_example/show.html', {'examples':examples})  


# 3. Valitaan jo lisätty esimerkkiolio muokattavaksi:
def edit(request, id):  
    example = Example.objects.get(id=id)  
    return render(request,'crud_example/edit.html', {'example':example})  


# 4. Tallennetaan muutokset esimerkkiolioon:
def update(request, id):  
    example = Example.objects.get(id=id)  
    form = ExampleForm(request.POST, instance = example)  
    if form.is_valid():  
        form.save()  
        return redirect("/")  
    return render(request, 'edit.html', {'example': example})  


# 5. Poistetaan esimerkkiolio
def delete(request, id):  
    example = Example.objects.get(id=id)  
    example.delete()  
    return redirect("/")  


def edit_popup(request):
    return render(request, 'crud_example/edit_popup.html')