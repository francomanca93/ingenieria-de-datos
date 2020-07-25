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
    '''ETL: Función para automatizar extracción de datos.
    
    Contiene un for loop que nos lleva a través del procedimiento automatizado en consola 
    para la ejecución de los archivos para la extracción de datos. '''

    logger.info('Starting extract process')
    for news_site_uid in news_sites_uids:
        subprocess.run(['python', 'main.py', news_site_uid], cwd='./extract')
        subprocess.run(['find', '.', '-name', '{}*'.format(news_site_uid),
                       '-exec', 'mv', '{}', '../transform/{}_.csv'.format(news_site_uid),
                       ';'], cwd='./extract')


def _transform():
    '''ETL: Función para automatizar la tranformación de datos.
    
    Contiene un for loop que nos lleva a través del procedimiento automatizado en consola 
    para la ejecución de los archivos para la transformación de datos. '''

    logger.info('Starting transform process')
    for news_site_uid in news_sites_uids:
        dirty_data_filename = '{}_.csv'.format(news_site_uid)
        clean_data_filename = 'clean_{}'.format(dirty_data_filename)
        subprocess.run(['python', 'main.py', dirty_data_filename], cwd='./transform')
        subprocess.run(['rm', dirty_data_filename], cwd='./transform')
        subprocess.run(['mv', clean_data_filename, '../load/{}.csv'.format(news_site_uid)],
                        cwd='./transform')



def _load():
    pass


if __name__ == '__main__':
    main()