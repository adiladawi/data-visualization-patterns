import os
import re

path = '/home/juannis/data-visualization-patterns/display-patterns/Discrete Quantities/Pruebas'
lstFiles = []
lstFilesR = []
lstDir = os.walk(path)   #os.walk()Lista directorios y ficheros
lib=dict()  

for root, dirs, files in lstDir:
    for fichero in files:
        (nombreFichero, extension) = os.path.splitext(fichero)
        if(extension == ".py"):
            lstFiles.append(nombreFichero+extension) 
        if(extension == ".R") or (extension == ".r"):
            lstFilesR.append(nombreFichero+extension)         

for file in lstFiles:
	archivo = open(file, "r") 
	contenido = archivo.read()
	patron = re.compile(r'\bimport\b')
	r=patron.findall(contenido)
 	lib[file]= str(len(r))
	archivo.close()

for file in lstFilesR:
	archivo = open(file, "r") 
	contenido = archivo.read()
	patron = re.compile(r'\blibrary\b')
	r=patron.findall(contenido)
 	lib[file]= str(len(r))
	archivo.close()

archivo = open("pruebas.md", "w")
archivo.write('| {:30}'.format('File')+' |{:>15}'.format('Library')+" | \n")
archivo.write( '|--------------------------------|----------------|'+'\n')
for l in lib:	
	archivo.write('| {:30}'.format(l)+' |{:>15}'.format(lib[l])+" | \n")
	print '{:30}'.format(l)+'{:>10}'.format(lib[l])	
archivo.close()


