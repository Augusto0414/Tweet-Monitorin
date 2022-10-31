# **Tweet Monitoring**

## **Pre-rrequisitos**

- Tener instalado Python

- Tener instalado una IDE

### **¿Como instalar Python?**

1. Descargue el instalador del archivo ejecutable de [Python](https://www.python.org/downloads/) para Windows x86-64

2. Iniciar la instalación ejecutando el archivo descargado Python-3.10.7.exe o
   Python-3.10.7-amd64.exe con doble clic. Si es necesario, confirmar la ejecución en la ventana de advertencia de seguridad de Abrir archivo.

3. Una vez iniciado el instalador, en la ventana Install Python 3.10.7 (64 bit) activar las casillas de las opciones: Install launcher for all users (recommended) y Add Python 3.10.7 to PATH. Después, continuar seleccionando la opción Customize installation. Choose Location and features.

4. En la ventana Optional features verificar que están activas todas las opciones y
   hacer clic en el botón **[Next]**.

5. En la ventana Advanced Options verificar que están activas las opciones de la imagen,
   escribir la ruta del directorio de instalación "C:\Python36" (o aceptar la ruta por defecto)
   y comenzar la instalación haciendo clic en el botón **[Install]**.

6. A continuación, después de unos segundos de espera, comenzará el proceso de instalación de Python.

7. En la ventana Setup was successful, una vez que ha concluido el proceso de instalación
   hacer clic en el botón **[Close]**. Desde esta ventana es posible acceder a un tutorial online de Python, a la documentación oficial del lenguaje y a información con las novedades de la presente versión.

### **¿Como instalar una IDE?**

En nuestro caso la IDE que usamos es VSCode pero la IDE queda a su elección:

1. Ve a la página de Microsoft [Visual Studio Code](https://code.visualstudio.com/) y haz clic en el botón 'Descargar Visual Studio Code' para descargar el archivo de instalación.

2. Abre el archivo de instalación .exe en tu carpeta de descargas para iniciar la
   instalación.

3. Lee y acepta el acuerdo de licencia. Haz clic en Next para continuar.

4. Puedes cambiar la ubicación de la carpeta de instalación o mantener la
   configuración predeterminada. Haz clic en Next para continuar.

5. Elige si deseas cambiar el nombre de la carpeta de accesos directos en el menú
   Inicio o si no deseas instalar accesos directos en absoluto. Haz clic en Next.

6. Selecciona las tareas adicionales, por ej. crear un icono en el escritorio o añadir opciones al menú contextual de Windows Explorer. Haz clic en Next.

7. Haz clic en Install para iniciar la instalación.

8. El programa está instalado y listo para usar. Haz clic en Finish para finalizar la instalación y lanzar el programa.

## **Instalación**

### **¿Como instalar la libreria de tweepy?**

---

La forma más fácil de instalar la última versión de PyPI es mediante el uso de pip:

```
pip install tweepy
```

Para usar el subpaquete, asegúrese de instalar con el extra:tweepy.asynchronousasync

```
pip install tweepy
```

También puede usar Git para clonar el repositorio desde GitHub para instalar la última versión de desarrollo:

```
git clone https://github.com/tweepy/tweepy.git
cd tweepy
pip install
```

Alternativamente, instale directamente desde el repositorio de GitHub:

```
pip install git+https://github.com/tweepy/tweepy.git
```

### **¿Como instalar la libreria de Dash?**

---

En su terminal, instale .dash

```
pip install dash
```

Esto también trae consigo la biblioteca de gráficos. Esta biblioteca está en desarrollo activo, por lo que debe instalarse y actualizarse con frecuencia.plotly

Si prefiere Jupyter notebook o JupyterLab como entorno de desarrollo, le recomendamos que instale jupyter-dash:

```
pip install jupyter-dash
```

Estos documentos están ejecutando la versión .dash2.6.1. Esta versión es compatible con Python 3. Las versiones de antes también eran compatibles con Python 2.dash2.0.0

También recomendamos instalar Pandas, que es requerido por Plotly Express y utilizado en
muchos de nuestros ejemplos.

```
pip install pandas
```
