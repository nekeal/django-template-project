from .base import *

SECRET_KEY = "secret_key"

# ------------- DATABASES -------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("POSTGRES_DB", "django_template_project"),
        "USER": env("POSTGRES_USER", "django_template_project"),
        "PASSWORD": env("POSTGRES_PASSWORD", "django_template_project"),
        "HOST": env("POSTGRES_HOST", "localhost"),
    }
}
