from pathlib import Path

from environs import Env

env = Env()

PROJECT_NAME = "django_template_project"

BASE_DIR = Path(__file__).parents[2]
APPS_DIR = BASE_DIR.joinpath(PROJECT_NAME)

DEBUG = True

ALLOWED_HOSTS = []

# ------------- APPS -------------
DJANGO_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "dbbackup",
    "rest_framework",
    "rest_flex_fields",
    "django_filters",
    "djoser",
    "rest_framework_simplejwt",
    "django_extensions",
    "celery",
    "webpack_loader",
]

LOCAL_APPS = ["django_template_project.accounts.apps.AccountsConfig"]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# ------------- MIDDLEWARES -------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ------------- URLS -------------
ROOT_URLCONF = "django_template_project.urls"
WSGI_APPLICATION = "django_template_project.wsgi.application"

# ------------- TEMPLATES -------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [APPS_DIR.joinpath("templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ------------- PASSWORDS -------------
AUTH_USER_MODEL = "accounts.CustomUser"

PASSOWRD_HASHERS = [
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
    "django.contrib.auth.hashers.BCryptPasswordHasher",
]

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# ------------- INTERNALIZATION -------------
LANGUAGE_CODE = "en-us"

TIME_ZONE = "Europe/Warsaw"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# ------------- STATIC -------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR.joinpath("public")

# ------------- MEDIA -------------
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR.joinpath("media")
