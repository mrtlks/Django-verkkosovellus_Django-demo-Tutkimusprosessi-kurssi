
from django.db import models

# Create your models here.

class Example(models.Model):
    id = models.AutoField(primary_key=True)
    attribute_1 = models.CharField(max_length=30)
    attribute_2 = models.CharField(max_length=30)


class Meta:  
    model = Example  #class Meta-luokalla voidaan määritellä taulun nimi (muuten django muodostaa sen automaattisesti)


