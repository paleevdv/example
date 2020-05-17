from logging import getLogger, Formatter
from logging.handlers import TimedRotatingFileHandler
import functools
from settings import LOG_APP, LOG_LEVEL, LOG_FILE_NAME, LOG_COUNT_BACKUP, LOG_ROTATE_TIME, LOG_FORMAT

LOGGER = getLogger(LOG_APP)
LOGGER.setLevel(LOG_LEVEL)

filehandler = TimedRotatingFileHandler("./app_logs/"+LOG_FILE_NAME,
                                               when=LOG_ROTATE_TIME,
                                               backupCount=LOG_COUNT_BACKUP,
                                               )

filehandler.setFormatter(Formatter(LOG_FORMAT))

LOGGER.addHandler(filehandler)

def decoLogo(function):

    @functools.wraps(function)
    def wraps(*args, **kwargs):

        LOGGER.debug(['start', function.__name__])
        try:
            answer = function(*args, **kwargs)
            LOGGER.debug(['successful completion', function.__name__])
            return answer
        except BaseException as e:

            LOGGER.error([e, function.__name__])
            LOGGER.error((args, kwargs))

            raise e

    return wraps