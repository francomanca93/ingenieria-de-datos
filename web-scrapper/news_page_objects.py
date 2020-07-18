import requests
import bs4

from common import config


class HomePage():
    '''Clase que va a representar la página principal de nuestra web'''

    def __init__(self, news_site, url):
        '''Constructor.  
        @param news_site
        @param url
        '''
        self._config = config()['news_sites'][news_site]
        self._queries = self._config['queries']
        self._html = None  # Pagina parseada con bs4

        self._visit(url)
    
    @property
    def article_links(self):
        ''' Función para obtener los links principales de la web a consultar

        @return set(link['href'] for link in link_list)
        '''
        link_list = []
        for link in self._select(self._queries['homepage_article_links']):
            if link and link.has_attr('href'):
                link_list.append(link)

        return set(link['href'] for link in link_list)

    def _select(self, query_string):
        ''' Funcion para obtener informacion de config.yaml

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