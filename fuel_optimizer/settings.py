import os
from pathlib import Path

# -------------------------------
# BASE
# -------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------------
# SECURITY
# -------------------------------
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key")
DEBUG = os.getenv("DEBUG", "True") == "True"

ALLOWED_HOSTS = ["*"]

# -------------------------------
# APPS
# -------------------------------
INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",
    "routes",
]

# -------------------------------
# MIDDLEWARE
# -------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
]

# -------------------------------
# URLS
# -------------------------------
ROOT_URLCONF = "fuel_optimizer.urls"

# -------------------------------
# TEMPLATES (IMPORTANT FIX)
# -------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {"context_processors": []},
    },
]

# -------------------------------
# WSGI
# -------------------------------
WSGI_APPLICATION = "fuel_optimizer.wsgi.application"

# -------------------------------
# DATABASE (simple)
# -------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# -------------------------------
# STATIC FILES
# -------------------------------
STATIC_URL = "/static/"

# -------------------------------
# DEFAULT AUTO FIELD
# -------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"