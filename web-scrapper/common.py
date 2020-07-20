import yaml

__config = None  # Variable global. Para cachear nuestra configuracion

def config():
    '''Función config() para leer el archivo config.yaml y regresarlo '''
    global __config
    
    if not __config:
        with open('config.yaml', mode='r') as f:
            __config = yaml.safe_load(f)
    
    return __config