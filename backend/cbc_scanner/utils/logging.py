import logging
from rich.logging import RichHandler
import os

def setup_logging():
    log_dir = os.path.join(os.path.dirname(__file__), "..", "..", "..", "data", "logs")
    os.makedirs(log_dir, exist_ok=True)
    
    logging.basicConfig(
        level="INFO",
        format="%(message)s",
        datefmt="[%X]",
        handlers=[
            RichHandler(rich_tracebacks=True),
            logging.FileHandler(os.path.join(log_dir, "app.log"))
        ]
    )

setup_logging()
