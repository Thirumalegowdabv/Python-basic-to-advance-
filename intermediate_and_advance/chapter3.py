# Logging

# Why Logging?

# When programs run, we often need to track events, errors, or debug information.

# Instead of using print(), Python provides the logging module, which is:

# More flexible

# Supports log levels (info, warning, error…)

# Can log to files, console, or even remote servers

#  Basic Logging
import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug("This is a DEBUG message")
logging.info("This is an INFO message")
logging.warning("This is a WARNING")
logging.error("This is an ERROR")
logging.critical("This is CRITICAL")

# Output:
# DEBUG:root:This is a DEBUG message
# INFO:root:This is an INFO message
# WARNING:root:This is a WARNING
# ERROR:root:This is an ERROR
# CRITICAL:root:This is CRITICAL


# By default, the level is WARNING, so you won’t see DEBUG and INFO unless you set it.

# Log Levels

# Python defines 5 standard levels:

# DEBUG → detailed info (for developers)

# INFO → general events (program is running fine)

# WARNING → something unexpected, but still works

# ERROR → something failed

# CRITICAL → serious issue, program may stop



# Logging to a File
import logging

logging.basicConfig(
    filename="app.log",      # log file
    filemode="w",            # overwrite each run ("a" for append)
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.DEBUG
)

logging.info("This will be written to a file")


# app.log will contain:

# 2025-09-21 12:30:25,123 - INFO - This will be written to a file



# Log Format & Variables

# We can customize log messages:

logging.basicConfig(
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s",
    level=logging.DEBUG
)

logging.warning("Disk space is low")


# %(asctime)s → time

# %(name)s → logger name

# %(levelname)s → log level

# %(message)s → log message



# Using Loggers Instead of root
logger = logging.getLogger("myApp")
logger.setLevel(logging.DEBUG)

logger.debug("Debugging...")
logger.info("App is running")

# Best practice: use getLogger() instead of relying on the root logger.



# Handlers

# Handlers define where logs go:

# Console (StreamHandler)

# File (FileHandler)

# HTTP, Socket, Syslog, etc.

# Example:

import logging

logger = logging.getLogger("myApp")
logger.setLevel(logging.DEBUG)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# File handler
file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.ERROR)

# Formatter
formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Add handlers
logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.debug("This goes to console (if >= INFO)")
logger.error("This goes to both console and file")




# Advanced Features
#  Multiple Modules (Best Practice)

# In a project:

# Each file/module gets its own logger.

# All loggers bubble up to a root logger (unless stopped).

# module1.py
import logging
logger = logging.getLogger(__name__)

def run():
    logger.info("Module 1 running")

# main.py
import logging
import module1

logging.basicConfig(level=logging.DEBUG)

module1.run()


# Rotating Log Files

# For long-running apps, logs can grow huge. Use RotatingFileHandler:

from logging.handlers import RotatingFileHandler

handler = RotatingFileHandler("app.log", maxBytes=2000, backupCount=5)

# Keeps logs in rotation (e.g., app.log, app.log.1, app.log.2…)



# Timed Rotation
from logging.handlers import TimedRotatingFileHandler

handler = TimedRotatingFileHandler("timed_app.log", when="midnight", interval=1, backupCount=7)

# Creates a new log file every midnight, keeps 7 days.



# Exception Logging
try:
    1 / 0
except Exception as e:
    logging.exception("An error occurred")


#  Captures stack trace automatically.

#  Config from File (YAML/JSON/INI)

# You can configure logging via config files (production style).
# Example using dictConfig:

import logging.config

config = {
    "version": 1,
    "formatters": {
        "detailed": {
            "format": "%(asctime)s | %(name)s | %(levelname)s | %(message)s"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "detailed",
            "level": "DEBUG"
        }
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG"
    }
}

logging.config.dictConfig(config)
logger = logging.getLogger("app")
logger.info("Config-based logging")




#  Best Practices 

# Don’t use print() in production → use logging.

# Always create a logger = logging.getLogger(__name__) in each module.

# Use handlers for flexibility (console, file, etc.).

# Use RotatingFileHandler or TimedRotatingFileHandler to avoid huge files.

# Use logger.exception() inside except blocks.

# Configure logging via dictConfig or fileConfig in real projects.