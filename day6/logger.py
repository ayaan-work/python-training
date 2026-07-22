#basic logging
import logging

logging.basicConfig(level=logging.INFO)

logging.debug("Debug message")
logging.info("Program started")
logging.warning("Low disk space")
logging.error("File not found")
logging.critical("Database crashed")
#Notice that the DEBUG message wasn't shown because the logging level is set to INFO.

# Logging levels indicate the importance of a message.

# Level	          Value	         Purpose
# DEBUG	          10	         Detailed information for developers
# INFO	          20	         General information about program execution
# WARNING	      30	         Something unexpected, but the program can continue
# ERROR	          40	         A serious problem that affects part of the program
# CRITICAL	      50	         A severe error that may stop the application

print("\n")

#formatter
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s  %(levelname)s-%(message)s',
    datefmt='%Y-%m-%D %H:%M:%S'
)

logging.info("Server started")

print("\n")


logger = logging.getLogger("myapp")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("day6/app.log")

logger.addHandler(file_handler)

logger.info("Application started")

# Logger → Creates log messages.
# Level → Decides how important a message is.
# Handler → Decides where the message goes.
# Formatter → Decides how the message looks.
# FileHandler → A handler that saves logs to a file.