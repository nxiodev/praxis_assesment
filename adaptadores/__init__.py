# Librerias Estandar
from pathlib import Path

# Librerías de Terceros
from dotenv import load_dotenv

env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)
