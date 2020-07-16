<div align="center">
  <h1>Ingeniería de datos con Python</h1>
</div>

<div align="center"> 
  <img src="readme_img/ingenieria-datos.png" width="">
</div>

# Introducción al documento

El contenido de este documento son **apuntes teoricos** y un proyecto **Web Scrapper** del [Curso de Ingeniería de datos con Python](https://platzi.com/clases/ingenieria-datos/) y busca ser una guía para futuros trabajos personales. El mismo está dictado por [David Aroesti](https://github.com/jdaroesti) del team [Platzi](https://platzi.com).

# Objetivos del documento

- **Teoria.** Plasmar los fundamentos de la ingenieria de datos.
- **Práctica.** Crea un Web Scrapper profesional siguiendo el flujo de trabajo de un Ingeniero de Datos.


# Tabla de contenido

- [Introducción](#Introducción)
    - [Introducción al curso](#Introducción-al-curso)
    - [¿Qué es la Ciencia e Ingeniería de Datos?](#¿Qué-es-la-Ciencia-e-Ingeniería-de-Datos?)
    - [Roles](#Roles)
    - [Configuración del ambiente](#Configuración-del-ambiente)
    - [Jupyter Notebooks](#Jupyter-Notebooks)
    - [Profundizando en tipos de datos](#Profundizando-en-tipos-de-datos)
    - [Fuentes de datos](#Fuentes-de-datos)
    - [ETL](#ETL)
- [Web scraping](#Web-scraping)
  - [Introducción a las tecnologías web](#Introducción-a-las-tecnologías-web)
  - [Realizar solicitudes HTTP con Python](#Realizar-solicitudes-HTTP-con-Python)
  - [¿Cómo trabajar con un documento HTML?](#¿Cómo-trabajar-con-un-documento-HTML?)
- [Pandas](#Pandas)
- [Intro a Sistemas de Datos](#Intro-a-Sistemas-de-Datos)
- [Contenido Bonus](#Contenido-Bonus)


## Introducción
### Introducción al curso

En este curso vamos a explorar cuál es el proceso que se sigue en la **ingeniería de datos**. Obtener obtener datos y datasets del mundo real de diferentes fuentes y lugares. Casi siempre estos datos vienen en un formato o estructura que no esta lista para el **análisis** adecuado.

La ingeniería de datos se preocupan principalmente por implementar los **pipelines** que permiten automatizar la obtención de datos y su posterior limpieza para que otros profesionales de los datos(científicos de datos o expertos en machine learning) puedan realizar su labor. **Son la primera parte de la cadena**.

Podrás entender el día a día de un ingeniero de datos y cómo colabora con el resto del equipo.

### ¿Qué es la Ciencia e Ingeniería de Datos?

La Ciencia de Datos es la disciplina que se encarga de extraer conocimiento de los datos disponible. Casi siempre cuando te realizas una pregunta sobre datos estas fuentes se encuentran escondidas, ocultas o de difícil acceso. A nuestro alrededor hay datos en tu computadora, mesa, reloj, etc.

Los datos están por todas partes.

La Ciencia de datos es multidisciplinaria. A diferencia de muchos otros ámbitos profesionales dentro del mundo de la tecnología cuando hablamos de un científico de datos es una persona que sabe de matemáticas, ingeniería de software y sabe de negocios.

Se apoya en: 
- **Computer science**. Las computadoras son la mejor herramienta para procesar datos. Se apoya de: 
    - Algoritmos
    - Estructura de datos
    - Visualizaciones que nos puede dar la computadora.
    - Conectar varias computadoras en paralelo en la nube, 
    - Programación.
- **Matemática estadística**
    - Regresiones
    - Inferencias
    - Identificación de variables y relación de variables.
- Tener **conocimiento del dominio**
    - Preguntar los correcto
    - Interpretar datos correctamente en función a las preguntas que hagamos.

<div align="center"> 
  <img src="readme_img/data-science.png" width="">
</div>

Herramientas donde se auxilia:

- Bases de Datos
    - SQL (MySQL, Postgres, etc.)
    - NoSQL (Cassandra, Spark, etc.)
- Análisis de texto y procesamiento de lenguaje natural (NLP)
- Análisis de redes
- Análisis numérico de datos y minado de datos
- Visualización de datos
    - No permite contar historias
    - Analizar rapidamente
    - Los humanos somos mas eficientes analizando datos gráficos.
- Machine learning e Inteligencia Artificial
- Análisis de señales digitales. 
    - Análisis de datos en tiempo real. 
- Análisis de datos en la nube (Big Data). Data center que podemos utilizar eficientemente para procesar grandes cantidades de datos

### Roles

Existen por lo menos tres diferentes roles para tener un pipeline completo de ciencia de datos. Este curso trata sobre el primer rol:

- **Data engineer**: Se encarga de obtener los datos, Limpiarlos y estructurarlos para posterior análisis, crear pipelines de análisis automatizado, utilización de herramientas en la nube, análisis descriptivo de los datos.

- **Data scientist**: Una vez tiene los datos se encarga de generar el análisis matemático de ellos, encontrar las relaciones entre las variables, las correlaciones, las causas y por último genera los modelos predictivos y prescriptivos.

- **Machine Learning engineer**: Se encarga de llevar las predicciones a escala, de subirlos a la nube y allí generar muchas predicciones. Se encarga de mantener la calidad del modelo.

<div align="center"> 
  <img src="readme_img/hierarchy.png" width="">
</div>

### Configuración del ambiente

[**Anaconda**](https://www.anaconda.com/) es una instalación de Python que ya trae preinstalado todos los paquetes necesarios para tu labor en la Ciencia de Datos, tiene más de **1400 paquetes**. Nos permite configurar ambientes virtuales para poder utilizar diferentes versiones de nuestros paquetes.

- Para conocer la versión y saber que lo tenemos instalado: 

`conda --version`

- Para ver todos los comandos que podemos usar usamos:

`conda --help` 

- Para ver una lista de todos los paquetes que Anaconda instaló.

`conda list` 


Una buena práctica es generar un **ambiente virtual** por cada proyecto, los ambientes virtuales nos permiten generar varios proyectos con diferentes versiones de la librería sin generarnos errores de compatibilidad. Tradicionalmente en Python se utiliza virtualenv

`conda create --name nombre_entorno`

- Instalar librerias:

`$ conda install nombre_libreria`

- En este caso usaremos las siguientes librerias:
  - **beautifulsoup4** = parsear y manipular HTML
  - **requests** = generar solicitudes a la web
  - **numpy** = análisis numéricos de nuestros datos
  - **pandas** = analizar, modificar, transformar datos y generar análisis descriptivos sobre los mismos
  - **matplotlib** = generar visualizaciones de nuestros datos
  - **yaml** =archivo similar a Json, permite generar algunas configuraciones

Al instalar las librerias se instalan dependendias para que estas funcionen.

- Para activar el ambiente que acabamos de crear: 

`conda activate nombre_entorno`

- Para salir 

`conda deactivate`

- Para ver una lista de los ambientes virtuales que tenemos:

`$ conda info --envs` o tambien `$ conda env list`

- Para ver todos paquetes de nuestro entorno virtual:

`$ conda list -n nombre_entorno`

- Para eliminar nuestro entorno virtual con todos nuestros paquetes

`$ conda remove --name nombre_entorno --all`

### Jupyter Notebooks

Algo interesante que tenemos con Anaconda es que nos trae [Jupyter Notebooks](https://jupyter.org/).

Jupyter Notebooks es un entorno de programación en el cual podemos mezclar ejecución de código en vivo, visualizaciones y añadir markdown.

- Para inicializar nuestro servidor de jupyter:

`$ jupyter notebook`

Jupyter Notebook tiene diferentes tipos de celdas en las cuales podemos escribir código o markdown. Si queremos ejecutar nuestro código hacemos `ctrl + enter` y si queremos ejecutar y añadir una nueva celda `shift + enter`.

- `ESC`: dentro de una celda entrar al modo de navegación. (el borde izquierdo de la celda se resalta en azul)
- `K`: mover hacia arriba
- `J`: mover hacia abajo
- `B`: Agregar nueva celda
- `M`: Convertir en MarkDown
- `P`: Acceder a la línea de comando
- `DD`: Eliminar Celda

Jupyter Notebook tiene dos modalidades, la modalidad de edición y navegación.

### Profundizando en tipos de datos

Los datos vienen en muchas formas y estas formas las podemos clasificar de diferentes maneras, permitiéndonos poder aplicar técnicas distintas a cada uno de los tipos de datos.

- Los primeros datos son los primitivos.
`int, str, bool, float, hex, oct, datetime, objetos especiales`

Tenemos otras clasificaciones como los datos estructurados, semi estructurados y no estructurados.

- Los **estructurados** son los más fáciles de acceder a su información.
  - Bases de datos
  - Data warehouse
- Los **semis estructurados** donde podemos usar las APIs
  - json API's
  - Datos tabulares (csv, excel)
- Los **No estructurados** son la mayoría de los datos que te vas a encontrar en tu desarrollo profesional.
  - HTML
  - Texto libre
  - Imagenes, audios, videos
  - Datos científicos

<div align="center"> 
  <img src="readme_img/tipos-datos.jpg" width="80%">
</div>

### Fuentes de datos

- **Web**

Es una mina enorme con datos financieros, de startups, del clima, precipitación fluvial, astronómicos, de negocios, etc.


- **APIs**

Endpoints que viven en la web y nos devuelven JSON. Por ejemplo, la API de twitter, google, facebook.

Todas las [API's de google](https://console.cloud.google.com/apis/library) que este nos ofrece.

- **User Analytics**

Son el comportamiento del usuario dentro de nuestra aplicaciones, algo similar a los que nos ofrece Google Analytics.

- **IoT**

El [IoT o Internet of Things](https://es.wikipedia.org/wiki/Internet_de_las_cosas) Se ha vuelto una mina espectacular en los últimos años. Como automóviles, sensores en edificios y todo aquello que se pueda conectar a internet. 

En los siguientes enlaces podemos encontrar gran cantidad de datset asi como tambien un buscado de estos desarrollado por google.

- [Dataset Search de Google](https://datasetsearch.research.google.com/)
- [Data Word](https://data.world/)
- [Kaggle](https://www.kaggle.com/)

### ETL

**ETL = Extract Transform Load**

Los procesos ETL son un término estándar que se utiliza para referirse al movimiento y transformación de datos. Se trata del proceso que permite a las organizaciones mover datos desde múltiples fuentes, reformatearlos y cargarlos en otra base de datos (denominada data mart o data warehouse) con el objeto de analizarlos. También pueden ser enviados a otro sistema operacional para apoyar un proceso de negocio.

Si separamos por puntos cada uno haría lo siguiente:
- **Extract**: Es el proceso de lectura de datos de diversas fuentes

  - Base de datos
  - CRM
  - Archivos CSV
  - Datasets públicos

- **Transform**: En este momento cuando nosotros tenemos que transformar los datos, tenemos que identificar datos faltantes o datos erróneos o una edad negativa. En esta etapa donde tenemos que identificar todos los problemas y solucionarlos.

  - Limpieza
  - Estructurado
  - Enriquecimiento.

- **Load**: Una vez transformados debemos insertarlos en el data warehouse

  - Depende del tipo de solución que se haya escogido

<div align="center"> 
  <img src="readme_img/etl.png" width="">
</div>


## Web scraping

### Introducción a las tecnologías web

Las tecnologías web en principio podemos pensarlas como el internet, pero el internet es mucho más grande, es la red de redes, la forma en la que millones de computadores se conectan entre ellas para transferirse información.

El internet también se compone de otros pedazos (entre parentesis sus protocolos) como telefonía(voip), mail(pop3, imap), compartir archivos(ftp). El internet es una red que une varias redes públicas, privadas, académicas, de negocios, de gobiernos, etc.

La web específicamente es un espacio de información en el cual varios documentos(y otros recursos web) se pueden acceder a través de URLs y vínculos(links). La comunicación se da a través del protocolo **HTTP**.

Elementos básicos de la web:

- **HTML**: nos da la estructura de la información. Es un lenguaje para anotar pedazos de información para que el navegador o otros tipos de programa puedan interpretar que tipo de información se encuentra ahí.
- **CSS**: nos permite darle colores, arreglar el texto y añadir diferentes elementos de presentación.
- **Javascript**: nos permite añadir interactividad y cómputo a nuestra web.
- **JSON**: Simplemente es una forma de transmitir datos entre servidores y clientes. Es la forma estándar en las que en la web y las aplicaciones se comunican con los servidores backend.

### Realizar solicitudes HTTP con Python

Para poder experimentar con la web necesitamos un método programático para solicitar URLs y obtener HTML

**Requests**: Nos permite generar solicitudes a la web dentro de Python y utilizar los diferentes verbos HTTP, normalmente utilizaremos el método **GET** porque vamos a traer datos.

`requests.get('url')` para hacer una solicitud a la web y nos devolverá un objeto `response`

Al hacer una solicitud HTTP necesitamos saber en que estado será la misma con `responde.status_code`. Las posibles respuestas son:

- 200 : OK - Petición correcta.
- 400 : Bad request - Petición incorrecta.
- 404 : Not found - Recurso no encontrado.

Estos códigos estan categorizados en los siguientes grupos:

- 1xx : Respuestas informativas (Ej: 100, 101, 102, etc.)
- 2xx : Peticiones correctas (Ej: 200, 201, 202, etc.)
- 3xx : Redirecciones (Ej: 300, 301, 302, etc.)
- 4xx : Errores en el lado del cliente (Ej: 400, 401, 402, etc.)
- 5xx : Errores en el lado del servidor (Ej: 500, 501, 502, etc.)

Todas las solicitudes HTTP tienen metadatos para que los diferentes sistemas y computadoras puedan entender de qué va la solicitud.

[Script de solicitudes a la web]()

### ¿Cómo trabajar con un documento HTML?

En el caso de Python la librería estándar para manipular los documentos HTML se llama **BeautifulSoup**.

**BeautifulSoup** nos ayuda a organizar gramaticalmente(parsear) el documento HTML para que tengamos una estructura con la cual podamos manejar y extraer información. BeautifulSoup convierte el string de HTML en un árbol de nodos para poder manipularlo.

Para manipularlo podemos usar los selectores CSS con `soup.select()`

[Script de extracción de datos en un documento HTML]()


## Pandas
## Intro a Sistemas de Datos
## Contenido Bonus

