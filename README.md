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
  - [Analizando un sitio web para encontrar las directivas a utilizar al hacer un web scrapping](#Analizando-un-sitio-web-para-encontrar-las-directivas-a-utilizar-al-hacer-un-web-scrapping)
  - [Solicitudes a la web - Requests](#Solicitudes-a-la-web---Requests)
  - [Implementando nuestro web scrapper - Configuración](#Implementando-nuestro-web-scrapper---Configuración)
  - [Implementando nuestro web scrapper - Obteniendo enlaces del front page](#Implementando-nuestro-web-scrapper---Obteniendo-enlaces-del-front-page)
  - [Implementando nuestro web scrapper - Obteniendo artículos](#Implementando-nuestro-web-scrapper---Obteniendo-artículos)
  - [Obtención de datos del Artículo](#Obtención-de-datos-del-Artículo)
  - [Persistiendo la información \"scrapeada\"](#Persistiendo-la-información-\"scrapeada\")
- [Pandas](#Pandas)
  - [Introducción a Pandas](#Introducción-a-Pandas)
  - [Estructura de datos - Series](#Estructura-de-datos---Series)
  - [Estructura de datos - DataFrames](#Estructura-de-datos---DataFrames)
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

[Script de solicitudes a la web](https://github.com/francomanca93/ingenieria-de-datos/blob/master/practicas/solicitud-extraccion-info-html.ipynb)

### ¿Cómo trabajar con un documento HTML?

En el caso de Python la librería estándar para manipular los documentos HTML se llama **BeautifulSoup**.

**BeautifulSoup** nos ayuda a organizar gramaticalmente(parsear) el documento HTML para que tengamos una estructura con la cual podamos manejar y extraer información. BeautifulSoup convierte el string de HTML en un árbol de nodos para poder manipularlo.

Para manipularlo podemos usar los selectores CSS con `soup.select()`

[Script de extracción de datos en un documento HTML](https://github.com/francomanca93/ingenieria-de-datos/blob/master/practicas/solicitud-extraccion-info-html.ipynb)

### Analizando un sitio web para encontrar las directivas a utilizar al hacer un web scrapping

Para poder desarrollar scrapers debemos entender los datos semi estructurados dados por el HTML para determinar qué tipo de selectores CSS necesitamos para sacar información.

### Solicitudes a la web - Requests

Un buen **Data engineer** utiliza los conceptos de la ingeniería de software para poder desarrollar sus programa. En nuestro caso para poder desarrollar nos apoyaremos de un patrón.

**Page Object Patter**: Es un patrón que consiste en esconder los _queries_ especificos que se utilizan para manipular un documento HTML detrás de un objeto que representa la página web.

Si estos _queries_ se añaden directamente al código principal, el código se vuelve frágil y va a depender mucho de la modificación que hagan a la web otras personas y arreglarlo se vuelve muy complicado.

### Implementando nuestro web scrapper - Configuración

Se crearán tres archivos para configurar el esqueleto del proyecto web scraper

- [config.yaml](https://github.com/francomanca93/ingenieria-de-datos/commits/master/web-scrapper/config.yaml): El siguiente archivo contendra la configuración y datos necesarios para screapear web sitios web que coloquemos en este.

  Los YAML es un formato para guardar objetos de datos con estructura de árbol. Sirven como archivos para configuración similares a json. La librería que usaremos para trabajar con estos es [pyyaml](https://pyyaml.org/wiki/PyYAMLDocumentation)

  [Un poco mas sobre YAML](https://fercontreras.com/conoce-que-es-un-yaml-e18e9d21ade4)

- [common.py](https://github.com/francomanca93/ingenieria-de-datos/commits/master/web-scrapper/common.py): Archivo .py para guardar funciones comunes que se utilizarán
- [main.py](https://github.com/francomanca93/ingenieria-de-datos/commits/master/web-scrapper/main.py): Archivo principal con el cual se hará interacción con la linea de comando. En el se llamará a otras clases, metodos y/o archivos. Se agregarán algunas librerias/módulos para poder:
  - Trabajar con la linea de comando. El módulo [argparse](https://rico-schmidt.name/pymotw-3/logging/index.html) sirve para análisis de opciones y argumentos de línea de comando.
  - Ver de una forma más amigable mensajes en la linea de comando. El módulo [logging](https://rico-schmidt.name/pymotw-3/logging/index.html) sirve para hacer informes de estados, error y mensajes informativos. 

### Implementando nuestro web scrapper - Obteniendo enlaces del front page

En esta sección lo que se hará es ir a la pagina principal a través de BeautifulSoup y luego identificar todos los vinculos que nos llevaran a los articulos de noticia principales.

- Se agrega el archivo [news_page_objects.py](https://github.com/francomanca93/ingenieria-de-datos/commit/30d5fb0df0606e11b43a6bad32c25518403c9a2e#diff-17475357362c0f9e134381cd0e104388): Este tiene una clase HomePage que va a representar la página principal de nuestra web. Tiene métodos para:
  - Obtener los links principales de la web a consultar.
  - Obtener informacion de config.yaml.
  - Parsear el html de la url que pasemos.

Para realizar una **request/response (solicitd/respuesta) http** se utilizará el módulo [requests](https://requests.readthedocs.io/es/latest/).

Para realizar perseado de una página web se utiliza BeautifulSoup. Mas información sobre la librería en el siguiente [link](https://code.tutsplus.com/es/tutorials/scraping-webpages-in-python-with-beautiful-soup-the-basics--cms-28211)

- Se instancio de la clase HomePage el objeto homepage para luego imprimir links principales.
- Se agregarón nuevas paginas para parsear y queries a selectores html. 

### Implementando nuestro web scrapper - Obteniendo artículos

Lo que se hará en esta sección es crear clases que representen a una página genérica y luego de esta heredarán nuestra Pagina principal y la página del artículo. 

Se agregarán nuevas clases en el archivo [news_page_objects.py](https://github.com/francomanca93/ingenieria-de-datos/commit/c4840816707527a56302b64da9bb5e0c2a18bd83#diff-17475357362c0f9e134381cd0e104388)
- `NewsPage()`: Clase que va a representar a nuestra web. Esta tiene los siguientes métodos
    - `_select`: Funcion para obtener informacion de config.yaml.
    - `_visit`: Función para parsear el html de la url que pasemos.
- `HomePage(NewsPage)`: Clase que va a representar la página principal de nuestra web. Hereda de NesPage(). Tiene un método principal.
    - `article_links`: Método para obtener los links principales de la web a consultar.
- `ArticlePage(NewsPage)`: Clase que va a representar un artículo de la web. Tiene dos métodos principales:
    - `body`: Método para seleccionar el cuerpo del artículo.
    - `title`: Método para seleccionar el título del artículo.

### Obtención de datos del Artículo
Hecha la abstraccion con las clases correspondientes para poder obtener los datos de un articulo de una pagina, lo que se hará es validar que los vinculos se encuentran en el formato correcto o convertirlo.
Luego se visitará cada pagina y se consultará el título y el cuerpo para ir armando el datasets.

Se recorrerá cada una de las url del homepage para saber si existe un articulo o no. Los viculos vienen de diversas formas:
- Completos y bien formados.
- Vinculos relativos
- Vinculos relativos a la raiz de la url

Se utilizará la libreria [**re**](https://docs.python.org/3/library/re.html#module-contents). Este nos permite generar expresiones regulares en Python para poder determinar cual de los vinculos es válido o no, y asi poder obtener toda la informacion.

- En main inicializamos a nuestro objeto articlePage
- Crearemos las siguientes funciones en [main.py](https://github.com/francomanca93/ingenieria-de-datos/commit/c1eb14e5ace4710f55bf1502bcfc5773757950d1#diff-c85a2c3c9e83e1b7b251b7905cf347e2)
  - `_fetch_article`: Función para buscar un artículo.
  - `_build_link`: Función que nos permitirá crear un link perfecto al cual podamos acceder. Crear un patron de expresion regulares para poder implementar la funcion
    - Utilizaremos dos objetos con un patron diferentes para detectar enlaces. **^** Indica que empieza la expresión regular
      - is_well_formed_link = re.compile(r'^https?://.+/.+$')  # https://example.com/hello
      - is_root_path = re.compile(r'^/.+$')  # /some-text

### Persistiendo la información \"scrapeada\"

La persistencia de información se trata de guardar en un archivo los datos que estamos minando de la web para luego manipularlos. 

Lo que hacemos en esta sección es agregar la siguiente función en [main.py](https://github.com/francomanca93/ingenieria-de-datos/commit/f760d915473181e0f579a1773f9948d45e34ae50#diff-c85a2c3c9e83e1b7b251b7905cf347e2):
- `_save_article`: Función para guarda en un csv el body de articulos screapeados.


## Pandas

### Introducción a Pandas

[**Pandas**](https://pandas.pydata.org/) nos otorga diversas facilidades para el **Data Wrangler** (““domados de datos””). Nos otorga dos estructuras de datos:

- **Series**: Es un array unidimensional que representa una columna.
- **DataFrame**: Es un conjunto de series que forman una tabla. Se pueden acceder a través de indices como una etiqueta(label) o pueden ser posicionales es decir 0 o índice 100. También pueden ser **rangos** o slices

Estas estructuras de datos **no son** contenedores de datos. En Pandas las utilizamos para: 
- Transformar y enriquecer nuestros datos.
- Manipular nuestros datos.
- Manejar los datos faltantes.
- Realizar operaciones aritméticas.
- Combinar diferentes dataframes en uno solo para obtener una nueva tabla.
- etc.

[**Pandas Cheat Sheet**](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/PandasPythonForDataScience.pdf)

### Estructura de datos - Series

**Series** es un vector unidimensional, para poder acceder a esta lista podemos usar posiciones o labels, siendo este último el preferido para manipular las series. Una diferencia importante sobre las listas de Python es que los datos son homogéneos, es decir **solo podemos tener un tipo de dato por cada Serie**.

Las Series se pueden crear a partir de cualquier secuencia(listas, tuplas, arrays de numpy y diccionarios).

En Python tenemos la filosofía del Duck Typing, si se ve como un pato y hace cuac, a ese animal le llamamos pato, si una serie se comporta una lista, se accede como una lista en principio deberíamos llamarla lista, pero esto no es así.

Una mejor aproximación para inicializar Series es utilizar diccionarios.

[Documentación oficial Pandas: Series](https://pandas.pydata.org/pandas-docs/stable/reference/series.html)

### Estructura de datos - DataFrames

**DataFrames** son simplemente una tabla donde las filas y las columnas tienen etiquetas, se puede construir de diferentes formas pero siempre debemos considerar que la estructura que necesitamos construir para inicializarla tiene que ser bidimensional. Una matriz y puede ser una lista de listas, lista de tuplas, un diccionario de Python u otro **DataFrame**.

Si solo tenemos una dimensión a eso no le llamamos **DataFrame**, le llamamos Serie. Cuando utilizamos un diccionario las llaves se convierten en las llaves de la columna.

[Documentación oficial Pandas: DataFrame](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html)


## Intro a Sistemas de Datos
## Contenido Bonus

