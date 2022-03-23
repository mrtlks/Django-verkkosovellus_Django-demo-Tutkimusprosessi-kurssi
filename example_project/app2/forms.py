
from django.forms import ModelForm
from .models import Example
from django.utils.translation import gettext_lazy as _

class ExampleForm(ModelForm):
   
    class Meta:  
       model = Example 
      # fields = "__all__"  #jos käyttöön halutaan kaikki kentät
       fields = ['attribute_1', 'attribute_2'] #jos halutaan valita tietyt kentät
       #fields = ['attribute_2']
       #https://docs.djangoproject.com/en/4.0/topics/forms/modelforms/
       #forms -luokalla ei ole save() -metodia joten on käytettävä ModelFormia

       # raise ValueError('ModelForm has no model class specified.') tulee jos tässä yrittää 
       #määritellä Kenttiä ExampleFormin alle

       #atribuuttien uudelleennimeäminen
       labels = {
            'attribute_1': _('Ominaisuus 1'),
            'attribute_2': _('Ominaisuus 2')
            }

#https://docs.djangoproject.com/en/dev/topics/forms/modelforms/#overriding-the-default-fields
#https://stackoverflow.com/questions/36905060/how-can-i-change-the-modelform-label-and-give-it-a-custom-name/36905090