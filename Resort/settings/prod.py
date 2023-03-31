from .base import *
import environ
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent
print(BASE_DIR)
env=environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

DEBUG = env("DEBUG")

ALLOWED_HOSTS = ["*"]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"