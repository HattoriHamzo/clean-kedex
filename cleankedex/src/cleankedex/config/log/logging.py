import logging
from logging import Formatter, Logger, StreamHandler
from cleankedex.config.settings.settings import settings

LOG_FORMAT: str = (
    "%(levelname) -10s %(asctime)s %(name) -30s %(funcName) "
    "-35s %(lineno) -5d: %(message)s"
)

# create logger
logger: Logger = logging.getLogger(__file__)
logger.setLevel(settings.LOG_LEVEL)

# create console handler and set level to debug
ch: StreamHandler = logging.StreamHandler()
ch.setLevel(settings.LOG_LEVEL)

# create formatter
formatter: Formatter = logging.Formatter(LOG_FORMAT)

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)
