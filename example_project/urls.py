"""example_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from example_project.app1 import views as account_views 
from example_project.app2 import views as crud_views
# koska sovelluksia on usempi, on niiden näkymille annettava nimi, jotta Django voi hakea oikean sovelluksen näkymän

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('', crud_views.home, name='home'), # määritellään home-sivupohjan osoite sekä annetaan nimi näkymälle
    path('signup/', account_views.signup, name='signup'),
    path('login_test/', account_views.test_login_required, name='login_test'),
    path('login_test2/', account_views.test_login_required2.as_view(), name='login_test2'),
    path('', crud_views.show, name='show'),  
    path('show/', crud_views.show, name='show'),  
    path('delete/<int:id>', crud_views.delete),  # olion id tarvitaan delete -näkymässä
    path('edit/<int:id>', crud_views.edit, name='edit'), # olion id tarvitaan edit -näkymässä
    path('', crud_views.edit_popup), 
    path('update/<int:id>', crud_views.update) # olion id tarvitaan update -näkymässä
    
]
