import logging

#logging settings
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler("app1.log"),
        logging.StreamHandler()
    ]
)

logger=logging.getLogger('ArithmeticApp')

def add(a,b):
    logger.debug(f'{a} + {b} = {a+b}')
    return a+b

def substract(a,b):
    logger.debug(f'{a} - {b} = {a-b}')
    return a-b

def multiply(a,b):
    logger.debug(f'{a} * {b} = {a*b}')
    return a*b

def divison(a,b):
    try:
        logger.debug(f'{a} / {b} = {a/b}')
        return a/b
    except ZeroDivisionError:
        logger.error('Divison by zero')
        return None

add(12,10)
substract(52,47)
multiply(12,4)
divison(13,0)