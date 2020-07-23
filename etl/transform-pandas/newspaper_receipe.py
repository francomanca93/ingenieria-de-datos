# Librerias estandar
import argparse
import hashlib
import logging
logging.basicConfig(level=logging.INFO)
from urllib.parse import urlparse

# Librerias externas
import pandas as pd


logger = logging.getLogger(__name__)


def main(filename):
    '''Función principal que trabajará con las funciones secundarias y que se utilizará en el entry point.
    
    Parameters
    -------
    - filename : str (path)
        Path del dataset en csv
    
    Returns
    -------
    - df : dataframe
        Retorna un dataframe

    '''
    logger.info('Starting cleaning process')

    df = _read_data(filename)
    newspaper_uid = _extract_newspaper_uid(filename)
    df = _add_newspaper_uid_column(df, newspaper_uid)
    df = _extract_host(df)
    df = _fill_missing_titles(df)
    df = _generate_uid_for_rows(df)
    df = _remove_new_lines_from_body(df)

    return df


def _read_data(filename):
    '''Función que para leera el archivo.
    
    Parameters
    ---------
    - filename : str 
        Nombre del archivo que vamos a utilizar
    
    Returns
    -------
    - pd.read_csv(filename) : dataframe
        Lectura del archivo. Devuelve un dataframe.
    '''
    
    logger.info('Reading file {}'.format(filename))

    return pd.read_csv(filename)


def _extract_newspaper_uid(filename):
    '''Función para extraer id del dataset. 
    Primera parte del nombre del archivo.
    
    Parameters
    ------- 
    - filename : str 
        Nombre del archivo al cual se le extraerá el newspaper_uid

    Returns
    -------
    - newspaper_uid : str
        Id que se colocará en la columna para identificación proveniente de datos.
    '''
    
    logger.info('Extracting newspaper_uid')
    newspaper_uid = filename.split('_')[0]

    logger.info('Newspaper uid detected: {}'.format(newspaper_uid))
    return newspaper_uid


def _add_newspaper_uid_column(df, newspaper_uid):
    '''Funcion para agregar comlumna newspaper_uid. 
    Con esta columna identificamos de que dataset vienen nuestros datos.
    
    Parameters
    ---------
    - df : dataframe
        Recibe dataset para trabajar con él.
    - newspaper_uid : str
        Nueva columna con el id del dataset.
    
    Return 
    ------
    - df : dataframe 
        Retorna el dataset con una nueva columna.
    '''

    logger.info('Filling newspaper_uid column with {}'.format(newspaper_uid))
    df['newspaper_uid'] = newspaper_uid

    return df


def _extract_host(df):
    '''Función para agregar una columna adicional que representa el host de donde se obtiene la noticia.
    
    Parameters
    ----------
    - df : dataframe
        Recibe el dataset para poder agregarle al mismo una columna.
    
    Return 
    -------
    - df : dataframe
        Devuelve el dataset con una columna adicional.
    '''
    logger.info('Extracting host from urls')
    df['host'] = df['url'].apply(lambda url: urlparse(url).netloc)

    return df


def _fill_missing_titles(df):
    '''Función para rellenar titulos vacios
    
    Parameters
    ----------
    - df : dataframe
        Recibe el dataset.
    
    Return 
    -------
    - df : dataframe
        Devuelve el dataset con una columna adicional.
    '''
    logger.info('Filling missing titles')
    missing_titles_mask = df['title'].isna()

    missing_titles = (df[missing_titles_mask]['url']
                        .str.extract(r'(?P<missing_titles>[^/]+)$')
                        .applymap(lambda title: title.split('-'))
                        .applymap(lambda title_word_list: ' '.join(title_word_list))
                      )

    df.loc[missing_titles_mask, 'title'] = missing_titles.loc[:, 'missing_titles']

    return df


def _generate_uid_for_rows(df):
    '''Función para generar uid para cada fila.
    
    Parameters
    ----------
    - df : dataframe
        Recibe el dataset.
    
    Return 
    -------
    - df : dataframe
        Devuelve el dataset con una columna adicional seteando la columna uid como identificador unico de la fila
    '''
    logger.info('Generating uid for each rows')
    uids = (df
            .apply(lambda row: hashlib.md5(bytes(row['url'].encode('utf-8'))), axis=1)
            .apply(lambda hash_object: hash_object.hexdigest())
            )
    df['uid'] = uids

    return df.set_index('uid')


def _remove_new_lines_from_body(df):
    '''Función para remover saltos de lineas de los articulos en la columna body
    
    Parameters
    ----------
    - df : dataframe
        Recibe el dataset.
    
    Return 
    -------
    - df : dataframe
        Devuelve el dataset con los articulos de la columna body modificada. 
    '''
    logger.info('Remove new lines from body')

    stripped_body = (df
                     .apply(lambda row: row['body'], axis=1)
                     .apply(lambda body: list(body))
                     .apply(lambda letters: list(map(lambda letter: letter.replace('\n', ' '), letters)))
                     .apply(lambda letters: ''.join(letters))
                    )
    df['body'] = stripped_body

    return df


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename',
                        help='The path to the dirty data',
                        type=str)
    
    args = parser.parse_args()

    df = main(args.filename)
    print(df)