import logging.config
from app.core.settings import settings
from app.core.enums import Environment
import logging

logger = logging.getLogger(__name__)

APP_LEVEL = "DEBUG" if settings.ENVIRONMENT == Environment.local else "WARNING"

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "custom_colored": {
            # Use Uvicorn's default formatter class
            "()": "uvicorn.logging.DefaultFormatter",
            "format": "{levelprefix} {asctime} {name}:{lineno} -> {message}",
            "datefmt": "%H:%M:%S",
            "use_colors": True,
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "level": APP_LEVEL,
            "formatter": "custom_colored",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
    },
    "loggers": {
        "app": { # Your custom logger name
            "handlers": ["console"],
            "level": APP_LEVEL,
            "propagate": False,
        }, 
        "main": { # Your custom logger name
            "handlers": ["console"],
            "level": APP_LEVEL,
            "propagate": False,
        },
        
    },
}



def setup_logging():
    logger.debug(f"APP_LEVEL={APP_LEVEL}")
    logging.config.dictConfig(LOGGING_CONFIG)