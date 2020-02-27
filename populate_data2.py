import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','nomina.settings')

import random
import django
django.setup()

from sistema.models import Persona, Empresa, Escala, Cargo
from faker import Faker

fakegen = Faker()


estado = ['trabajando','desempleado']

escalaz = ['Escala Nivel 1','Escala Nivel 2','Escala Nivel 3','Escala Nivel 4','Escala Nivel 5']


def populate(N=1):

	for entry in range(N):

		estados = random.choice(estado)
		empresa = Empresa.objects.first()
		escalando = escalaz[entry]

		fake_cedula = fakegen.ean8()
		fake_apellido = fakegen.last_name()
		fake_nombre = fakegen.first_name()
		fakejob = fakegen.job()
		escalat= Empresa.objects.get(N)


		# if entry>0:
		# 	for grados in range(N):
		# 		for pasos in range(N):
		# 			sueldo = fakegen.ean(length=8)
		# 			escala= Escala.objects.get_or_create(escala=(escalando),grado=(grados),paso=(pasos),sueldo=sueldo, cod_empresa=empresa)




		personas = Persona.objects.get_or_create(status=estados, cedula=fake_cedula, apellido_1=fake_apellido, nombre_1=fake_nombre, cod_empresa=empresa)
		cargos = Cargo.objects.get_or_create(cod_escala=escalat, des_cargo=fakejob, cod_empresa=empresa)
		print(cargos)
		print(personas)


if __name__ == '__main__':

	print("popula")
	populate(4)
	print("populating complete")



