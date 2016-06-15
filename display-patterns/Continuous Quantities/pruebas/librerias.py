import os
import re

class pruebas:
	nombre=""
	lib=0
	loc=0

	def __init__(self, nombre, lib):
		self.nombre=nombre
		self.lib=lib
		self.loc=0
	
	def SetLoc(self,loc):
		self.loc=loc



if __name__ == '__main__':

	path = 'home/sustaita/Documentos/git/data-visualization-patterns/display-patterns/Continuous Quantities/pruebas'
	lstDir = os.walk(path)   #os.walk()Lista directorios y ficheros
	lstFiles = []
	lstFilesR = []
	lib=dict()
	lst=[]

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
		p=pruebas(file,len(r))
		lst.append(p)
		archivo.close()

	for file in lstFilesR:
		archivo = open(file, "r")
		contenido = archivo.read()
		patron = re.compile(r'\blibrary\b')
		r=patron.findall(contenido)	 	
	 	p=pruebas(file,len(r))
	 	lst.append(p)
		archivo.close()

	archivo = open("pruebas.txt", "r")
	for line in archivo.readlines():		
		for l in lst:				
			if not line.find(l.nombre)==-1:			
				l.SetLoc(line[-5:-1])

	
	archivo = open("pruebas.md", "w")
	archivo.write('| {:30}'.format('File')+' |{:>15}'.format('Library')+' |{:>15}'.format('LOC')+" | ")
	archivo.write( '|--------------------------------|----------------|----------------|'+'\n')
	for l in lst:	
		archivo.write('| {:30}'.format(l.nombre)+' |{:>15}'.format(str(l.lib))+' |{:>15}'.format(str(l.loc))+" | \n")	
	archivo.close()
