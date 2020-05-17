from logging import INFO
import configparser

CONFIG = configparser.ConfigParser()
CONFIG.read(f'conf')


LINKS = ['www.example.ru',]
#-----------{sql}-------------------------
DATABASE_URL = f'postgresql+psycopg2://{CONFIG["SQL"]["user"]}:' \
               f'{CONFIG["SQL"]["password"]}@{CONFIG["SQL"]["host"]}/{CONFIG["SQL"]["database"]}'
DB_TABLE_NAME = 'example'
DB_SEQUENCE_NAME = 'example_id_seq'
#-----------{sql}-------------------------

#-----------{log}-------------------------
LOG_APP = 'example_app'
LOG_LEVEL = INFO
LOG_FILE_NAME = 'app_log.log'
LOG_COUNT_BACKUP = 5
LOG_ROTATE_TIME = 'midnight'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
#-----------{log}-------------------------