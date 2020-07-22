import requests
import bs4

from common import config


class NewsPage():
    '''Clase que va a representar a nuestra web'''

    def __init__(self, news_site, url):
        '''Constructor.  
        @param news_site
        @param url
        '''
        self._config = config()['news_sites'][news_site]
        self._queries = self._config['queries']
        self._html = None  # Pagina parseada con bs4
        self._url = url

        self._visit(url)

    def _select(self, query_string):
        ''' Funcion para obtener informacion de config.yaml

        @param query_string: String del query tomado del config.yaml
        @return self._html.select(query_string)
        '''
        return self._html.select(query_string)

    def _visit(self, url):
        ''' Función para parsear el html de la url que pasemos
        @param url: url de la página que vamos a parsear
        '''
        response = requests.get(url)

        response.raise_for_status()  # Metodo que nos muestra un error si la solicitud no fue concluida correctamente

        self._html = bs4.BeautifulSoup(response.text, 'html.parser')


class HomePage(NewsPage):
    '''Clase que va a representar la página principal de nuestra web.
    Hereda de NewsPage'''

    def __init__(self, news_site, url):
        super().__init__(news_site, url)
    
    @property
    def article_links(self):
        ''' Método para obtener los links principales de la web a consultar

        @return set(link['href'] for link in link_list)
        '''
        link_list = []
        for link in self._select(self._queries['homepage_article_links']):
            if link and link.has_attr('href'):
                link_list.append(link)

        return set(link['href'] for link in link_list)


class ArticlePage(NewsPage):
    ''' Clase que va a representar un artículo de la web.
    Hereda de NewsPage
    Métodos principales
    - body: Cuerpo del artículo
    - title: Título del artículo
    '''
    def __init__(self, news_site, url):
        super().__init__(news_site, url)

    @property
    def url(self):
        ''' Método para leer y agregar el link del artículo. 
        El mismo es leido y utilizado en la variable csv_headers (Line 55 - main.py) '''
        result = self._url
        return result

    @property
    def body(self):
        ''' Método para seleccionar el cuerpo del artículo'''
        result = self._select(self._queries['article_body'])
        return result[0].text if len(result) else ''  # Programación defensiva. 

    @property
    def title(self):
        ''' Método para seleccionar el título del artículo'''
        result = self._select(self._queries['article_title'])
        return result[0].text if len(result) else ''  # Programación defensiva. 

