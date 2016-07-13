EXPERIMENTO
===================

### Métricas

* **Líneas de Código Fuente (SLOC: Source Lines of Code)**
De acuerdo a Conte, et al (1986) una línea de código es cualquier línea de texto en un programa que no sea una línea en blanco o un comentario [^1].
* **Número de Librerías, Módulos o Paquetes Externos Requeridos**
Se refiere al número de librerías, módulos o paquetes externos al núcleo del lenguaje, que se requieren para poder crear un gráfico (Mora-Soto et al, 2016)[^2].

### Procedimiento 

El procedimiento que se utilizo para realizar el experimento fue el siguiente:

1. Crear la carpeta "Pruebas" donde se guardan los resultados, . 
2. Hacer un archivo en R o Python por cada patron y  libreria. Guardar los archivos en la carpeta anterior .   
2. Contar SLOC  por cada archivo en R o Python haciendo uso de CLOC (Counter Lines of Code). Y se guarda la salida del reporte  en el archivo prueba.txt  haciendo uso del siguiente comando.
	* cloc --report-file=pruebas.txt Pruebas
3. Copiar el archivo librerias.py y  pruebas.txt en la carpeta "Pruebas".
4. Modificar la ruta para los archivos, en el archivo librerias.py  por la actual.
5. Ejecutar el archivo librerias.py

### Resultados

Los resultados de las metricas utilizadas se muestran en el archivo pruebas.md.

----------




Referencias
--------------------

[^1]: Conte, S. D., Dunsmore, H. E., & Shen, V. Y. (1986). Software Engineering Metrics and Models. Redwood City, CA, USA: Benjamin-Cummings Publishing Co., Inc.

[^2]:  Mora-Soto, A, Garcia-Fernandez, A., Mota-Garcia, M.J., Sustaita, L.A. (2016) A Survey for Software Metrics to Compare Statistical and Mathematics Oriented Programming Language. Centro de Investigación en Matemáticas, A.C


