# Librerias estadar
import argparse  #  Libreria estandar para análisis de opciones y argumentos de línea de comando
import csv
import datetime
import logging  # Libreria estandar para informe de estado, error y mensajes informativos
import re  # Módulo de expresiones regulares (re = regular expression)

# Librerias para exceptions
from requests.exceptions import HTTPError
from urllib3.exceptions import MaxRetryError
import socket

# Módulos própios
import news_page_objects as news
import common

# Objetos para informes por consola.
logging.basicConfig(level=logging.INFO)  # Configuración básica de logging
logger = logging.getLogger(__name__)

# Objetos para guardar expresiones regulares 
is_well_formed_link = re.compile(r'^https?://.+/.+$')  # https://example.com/hello
is_root_path = re.compile(r'^/.+$')  # /some-text


def _news_scraper(news_site):
    ''' Función para hacer un scraper a una pagina web sobre noticias.
    @param news_site: Sitio que queremos buscar según los que tengamos en config.yaml'''
    host = common.config()['news_sites'][news_site]['url']

    logging.info('Beginning scraper for {}'.format(host))
    homepage = news.HomePage(news_site, host)

    articles = []
    for link in homepage.article_links:
        article = _fetch_article(news_site, host, link)

        if article:
            logger.info('Article ferched!!')
            articles.append(article)

    _save_article(news_site, articles)


def _save_article(news_site, articles):
    ''' Función para guarda en un csv body de articulos screapeados.
    - @param news_site: Sitio que vamos a scrapear
    - @param articles: Lista de articulos
    - @return: Retorna un archivo csv como dataset
    '''
    now = datetime.datetime.now().strftime("%Y_%m_%d")
    out_file_name = '{news_site}_{datetime}_articles.csv'.format(
        news_site=news_site,
        datetime=now)
    csv_headers = list(filter(lambda property: not property.startswith('_'), dir(articles[0])))

    with open (out_file_name, mode='w+') as f:
        writer = csv.writer(f)
        writer.writerow(csv_headers)

        for article in articles:
            row = [str(getattr(article, prop)) for prop in csv_headers]
            writer.writerow(row)


def _fetch_article(news_site, host, link):
    ''' Función para buscar un artículo.
    @param news_site: Sitio nuevo donde se buscará el artículo
    @param host: 
    '''
    logger.info('Start fetching article at {}'.format(link))  # Mensaje en consola

    article = None
    try:
        article = news.ArticlePage(news_site, _build_link(host, link))
    except(HTTPError, MaxRetryError, socket.error) as e:
        logger.warning('Error while fetching the article', exc_info=False)

    if article and not article.body:
        logger.warning('Invalid article. There is no body')
        return None
    
    return article


def _build_link(host, link):
    ''' Funcion para construir el link y poder usarlo.
    @param host
    @param link
    @return link directamente; se forman los link con expresiones regulares.
    '''
    if is_well_formed_link.match(link):
        return link
    elif is_root_path.match(link):
        return '{}{}'.format(host, link)
    else:
        return '{host}/{uri}'.format(host=host, uri=link)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()  # Parseador de argumentos

    news_site_choices = list(common.config()['news_sites'].keys())
    parser.add_argument('news_site', 
                        help='The news site that you want to scrape',
                        type=str,
                        choices=news_site_choices)
    
    args = parser.parse_args()
    _news_scraper(args.news_site)