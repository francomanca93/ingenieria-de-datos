# Librerías estandar
import argparse
import logging
logging.basicConfig(level=logging.INFO)

# Librerias exteriores
import pandas as pd

# Módulos propios
from article import Article
from base import Base, engine, Session

logger = logging.getLogger(__name__)


def main(filename):
    '''Funcón principal que nos permite crear el schema, tomar datos del csv y pasarlo a un .db

    Parameter
    --------
    - filename : str
        Nombre del dataset csv
    
    Return
    -------
    - database : database from sqlite
    '''
    Base.metadata.create_all(engine)  # Nos genera el schema
    session = Session()  # Generamos nuestra sesion
    articles = pd.read_csv(filename)

    for index, row in articles.iterrows():  # Comenzamos a iterar por todos elementos del archivo
        logger.info('Loading article uid {} info DB'.format(row['uid']))
        article = Article(row['uid'],
                          row['body'],
                          row['host'],
                          row['newspaper_uid'],
                          row['n_token_body'],
                          row['n_token_title'],
                          row['title'],
                          row['url'],)
        session.add(article)

    session.commit()
    session.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename',
                        help='The file you want to load into the db',
                        type=str)
    
    args = parser.parse_args()

    main(args.filename)