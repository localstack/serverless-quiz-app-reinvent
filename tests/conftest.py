import logging
import sys

logging.getLogger("urllib3").setLevel(logging.WARNING)

logging.basicConfig(
    level=logging.DEBUG,
    stream=sys.stdout,
)
