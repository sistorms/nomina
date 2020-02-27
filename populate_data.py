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
		entrada = entry+1
		fake_cedula = fakegen.ean8()
		fake_apellido = fakegen.last_name()
		fake_nombre = fakegen.first_name()
		fakejob = fakegen.job()
		


		if entry>0:
			for grados in range(N):
				for pasos in range(N):
					sueldo = fakegen.ean(length=8)
					escala= Escala.objects.get_or_create(escala=(escalando),grado=(grados),paso=(pasos),sueldo=sueldo, cod_empresa=empresa)


		escalat= Escala.objects.get(pk=entrada)

		personas = Persona.objects.get_or_create(status=estados, cedula=fake_cedula, apellido_1=fake_apellido, nombre_1=fake_nombre, cod_empresa=empresa)
		cargos = Cargo.objects.get_or_create(cod_escala=escalat, des_cargo=fakejob, cod_empresa=empresa)
		print(cargos)
		print(personas)


if __name__ == '__main__':

	print("popula")
	populate(2)
	print("populating complete")



obj = Empleado.objects.filter(cod_rac=4).update(cedula=2656564)


asgiref==3.2.3
astroid==2.3.3  
cachetools==4.0.0
colorama==0.4.3  
Django==3.0.3
django-adminlte2==0.4.1
django-appconf==1.0.3  
django-baton==1.5.7
django-image-cropping==1.3.0
django-phone-field==1.8.0
django-suit==2.0a1
django-tabbed-admin==1.0.4
easy-thumbnails==2.7
factory-boy==2.12.0
Faker==4.0.0  
google-api-python-client==1.7.11
google-auth==1.11.0
google-auth-httplib2=0.0.3
httplib2==0.17.0
isort==4.3.21
lazy-object-proxy==1.4.3
mccabe==0.6.1
oauth2client==1.5.2
Pillow==7.0.0
pyasn1==0.4.8
pyasn1-modules==0.2.8
pylint====2.4.4
python-dateutil==2.8.1  
pytz==2019.3
rsa==4.0
setuptools==45.2.0
six==1.14.0
sqlparse===0.3.0
text-unidecode==1.3
typed-ast==1.4.1  
uritemplate==3.0.1
wheel==0.34.2
wrapt==1.11.2