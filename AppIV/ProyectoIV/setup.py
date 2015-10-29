from setuptools import setup
#Importamos desde el paquete setuptools y definimos la funcion setup
#Esta funcion le declaramos el nombre, version, la descripcion
#La unica complicacion es que en la variable package debemos de ponerle el destino
#de la carpeta donde tengamos definida la aplicacion y rellenar en "install_requires"
#los paquetes que necesitamos.
setup(name='IV',
    version='0.0.1',
    description='Preparando proyecto de tests',
    url='https://github.com/reyic/AppIV.git',
    author='Alejandro Jose Reyes Portellano',
    author_email='reyiczd@gmail.com',
    license='GNU General Public License',
    packages=['ProyectoIV'],
    install_requires=[
        'django',
        'wheel',
    ],
    zip_safe=False)