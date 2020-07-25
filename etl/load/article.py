from sqlalchemy import Column, String, Integer
from base import Base

class Article(Base):
    ''' Clase para estructurar los datos en una base de datos.
    Hereda de Base.

    Attributes
    -------
    - id : str
    - body: str
    - host: str
    - newspaper_uid : str
    - n_token_body : int
    - n_token_title : int
    - title : str
    - url : str

    Methods
    -------
    - __init__ : Constructor

    ''' 
    __tablename__ = 'articles'

    id = Column(String, primary_key=True)
    body = Column(String)
    host = Column(String)
    title = Column(String)
    newspaper_uid = Column(String)
    n_token_body = Column(Integer)
    n_token_title = Column(Integer)
    url = Column(String, unique=True)  # Constrain

    def __init__(self,
                uid,
                body,
                host,
                newspaper_uid,
                n_token_body,
                n_token_title,
                title,
                url):
        ''' Constructor de la clase articles
        
        Attributes
        -------
            - id : str
            - body: str
            - host: str
            - newspaper_uid : str
            - n_token_body : int
            - n_token_title : int
            - title : str
            - url : str
        '''
        self.id = uid
        self.body = body
        self.host = host
        self.newspaper_uid = newspaper_uid
        self.n_token_body = n_token_body
        self.n_token_title = n_token_title
        self.title = title
        self.url = url