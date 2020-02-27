import random

import factory
from factory.django import DjangoModelFactory
from django.utils.text import slugify
from faker import Faker

from . import models

fake = Faker()


class PersonaFactory(DjangoModelFactory):
    class Meta:
        model = models.Persona
    

    cedula = factory.Faker('random_number', digits=6)
    apellido_1 = factory.Faker('last_name')  
    nombre_1 = factory.Faker('first_name')  
    nombre_2 = factory.Faker('first_name')
    apellido_2 = factory.Faker('last_name')  
    fecha_nacimiento = factory.Sequence(lambda n: datetime.date(2000, 1, 1) + datetime.timedelta(days=n))
    edad = factory.Faker('random_number', digits=2)  
    ocupacion = factory.Faker('job')
    cargo_opt = factory.Faker('job')
    email = factory.Faker('email')
    telf = factory.Faker('phone')

