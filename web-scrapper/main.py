import argparse  #  Libreria estandar para análisis de opciones y argumentos de línea de comando
import logging  # Libreria estandar para informe de estado, error y mensajes informativos
logging.basicConfig(level=logging.INFO)
import re  # Módulo de expresiones regulares (re = regular expression)

from requests.exceptions import HTTPError
from urllib3.exceptions import MaxRetryError

import news_page_objects as news
import common


logger = logging.getLogger(__name__)
is_well_formed_link = re.compile(r'^https?://.+/.+$')  # https://example.com/hello
is_root_path = re.compile(r'^/.+$')  # /some-text


def _news_scraper(news_site):
    host = common.config()['news_sites'][news_site]['url']

    logging.info('Beginning scraper for {}'.format(host))
    homepage = news.HomePage(news_site, host)

    articles = []
    for link in homepage.article_links:
        article = _fetch_article(news_site, host, link)

        if article:
            logger.info('Article ferched!!')
            articles.append(article)
            print(article.title)
    
    print(len(articles))


def _fetch_article(news_site, host, link):
    ''' Función para buscar un artículo.
    @param news_site: Sitio nuevo donde se buscará el artículo
    @param host: 
    '''
    logger.info('Start fetching article at {}'.format(link))  # Mensaje en consola

    article = None
    try:
        article = news.ArticlePage(news_site, _build_link(host, link))
    except(HTTPError, MaxRetryError) as e:
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