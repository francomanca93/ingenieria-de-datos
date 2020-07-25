# Librerias estandar
import logging
logging.basicConfig(level=logging.INFO)
import subprocess  # Nos permite manipular directamente archivos de terminal. Una terminal en python

logger = logging.getLogger(__name__)
news_sites_uids = ['eluniversal', 'elpais', 'clarin']  # Periodicos que vamos a scrapear


def main():
    '''Función principal ETL.'''
    _extract()
    _transform()
    _load()


def _extract():
    pass


def _transform():
    pass


def _load():
    pass


if __name__ == '__main__':
    main()