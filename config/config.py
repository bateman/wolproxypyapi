"""Configuration file for the application."""

import configparser
import logging
import logging.config
import os
from pathlib import Path

import pretty_errors
from dotenv import load_dotenv
from rich.logging import RichHandler

# Directories
BASE_DIR = Path(__file__).parent.parent.absolute()
CONFIG_DIR = Path(BASE_DIR, "config")
LOGS_DIR = Path(BASE_DIR, "logs")

# Create dirs
LOGS_DIR.mkdir(parents=True, exist_ok=True)


# Use config file to initialize rich logger
logging.config.fileConfig(Path(CONFIG_DIR, "logging.config"))
logger = logging.getLogger("root")
logger.handlers[0] = RichHandler(markup=True)

# Configure error formatter
pretty_errors.configure(
    separator_character="*",
    filename_display=pretty_errors.FILENAME_EXTENDED,
    line_number_first=True,
    display_link=True,
    lines_before=5,
    lines_after=2,
    line_color=pretty_errors.RED + "> " + pretty_errors.default_config.line_color,
    code_color="  " + pretty_errors.default_config.line_color,
    truncate_code=True,
    display_locals=True,
)

# Use config file to initialize Uvicorn logger
api_config = configparser.ConfigParser()
with open(Path(CONFIG_DIR, "api.config"), encoding="UTF-8") as f:
    api_config.read_file(f)


# Load environment variables
load_dotenv()
API_KEY = os.environ.get("API_KEY") or os.urandom(24).hex()
