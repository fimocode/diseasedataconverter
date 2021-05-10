import logging as default_logging

logging = default_logging
LOG_FORMAT = '%(asctime)s (%(levelname)s) : [%(name)s],%(filename)s:%(lineno)d %(message)s'
logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, datefmt='%Y-%m-%d %H:%M:%S')
