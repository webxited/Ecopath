import environ
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent
print(BASE_DIR)
env=environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# check if value of 'environmnet' is 'development' then import .dev.py else import .prod.py
if env('ENVIRONMENT') == 'DEVELOPMENT':
    from .dev import *
if env('ENVIRONMENT') == 'PRODUCTION':
    from .prod import *