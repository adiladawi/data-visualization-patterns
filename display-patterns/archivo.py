import re
archivo = open("bar.py", "r") 
contenido = archivo.read()
patron = re.compile(r'\bimport\b')
r=patron.findall(contenido)
archivo.close()
archivo = open("p.md", "w")
archivo.write('Numero de librerias: '+str(len(r)))
archivo.close()

