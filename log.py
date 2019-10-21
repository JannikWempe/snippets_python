import os
import sys
import logging
import logging.handlers


def create_logger(
    name: str,
    logfile_path: str,
    logfile_name: str,
    log_level_to_file: [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL] = logging.DEBUG,
    log_level_to_stderr: [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL, None] = None,
) -> logging.Logger:
    """Create and return a custom logger."""

    allowed_log_levels = [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL]
    # check provided log level
    if log_level_to_file not in allowed_log_levels:
        raise LookupError(f"Unsupported log_level: {log_level_to_file}")
    if log_level_to_stderr not in [*allowed_log_levels, None]:
        raise LookupError(f"Unsupported log_level_to_console: {log_level_to_stderr}")

    # create logile_path folder if it doesn't exist
    if not os.path.exists(logfile_path):
        os.mkdir(logfile_path)

    # instantiate a logger
    logger = logging.getLogger(name)
    # set log level
    logger.setLevel(log_level_to_file)
    # set log format
    log_format = "%(asctime)s | %(name)-12s | %(levelname)-8s : %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"
    formatter = logging.Formatter(log_format, date_format)
    # log to file
    file_handler = logging.FileHandler(os.path.join(logfile_path, logfile_name))
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    # log to console
    if log_level_to_stderr:
        stream_handler = logging.StreamHandler(sys.stderr)
        stream_handler.setFormatter(formatter)
        stream_handler.setLevel(log_level_to_stderr)
        logger.addHandler(stream_handler)

    return logger

# EXAMPLE USAGE
logfile_path = os.path.dirname(os.path.abspath(__file__))
logfile_name = "testlog.log"
logger = create_logger("mylogger", logfile_path, logfile_name, logging.DEBUG, logging.DEBUG)
logger.error("Debug error.")
