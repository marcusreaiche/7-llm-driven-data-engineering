import os
from pathlib import Path


OPENAI_API_KEY = "OPENAI_API_KEY"
# Gets the API key from the environment
def get_api_key():
    API_KEY = os.environ.get(OPENAI_API_KEY)
    if API_KEY is None:
        raise ValueError(f"You need to specify {OPENAI_API_KEY} environment variable!")
    return API_KEY


# Set the API key from the environment
def set_api_key_from_dot_env():
    """
    Set OPENAI API key from .env
    """
    SRC_DIR = Path(os.path.dirname(__file__))
    DOT_ENV_PATH = SRC_DIR / ".." / ".env"
    if DOT_ENV_PATH.is_file():
        with open(DOT_ENV_PATH, "rt") as fp:
            for row in fp:
                row = row.strip()
                comment_index = row.find('#')
                if comment_index != -1:
                    row = row[:comment_index].strip()
                if '=' in row:
                    key, val = row.split('=', maxsplit=2)
                    if key == OPENAI_API_KEY:
                        os.environ[OPENAI_API_KEY] = val
