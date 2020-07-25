from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
# Nos permite tener acceso a funcionales ORM, nos permite trabjar con objetos de python y no con queries SQl directamente.
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///newspaper.db') 

Session = sessionmaker(bind=engine)

Base = declarative_base()  # Clase base de la cual van a extender todos nuestro modelos