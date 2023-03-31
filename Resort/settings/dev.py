from .base import *
import environ
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent
print(BASE_DIR)
env=environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG")

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]