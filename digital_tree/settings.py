from pathlib import Path

from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config("SECRET_KEY")

DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = config("ALLOWED_HOSTS").split(" ")


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    # 3rd party
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "crispy_forms",
    "django_extensions",
    # local apps
    "apps.common",
    "apps.users",
    "apps.core",
    "apps.products",
    "apps.stocks",
    "apps.portfolio",
    "apps.mensagens",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "digital_tree.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
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

WSGI_APPLICATION = "digital_tree.wsgi.application"


# if DEBUG:
#     DATABASES = {
#         "default": {
#             "ENGINE": "django.db.backends.sqlite3",
#             "NAME": BASE_DIR / "db.sqlite3",
#         }
#     }
# else:
DATABASES = {
    "default": {
        "ENGINE": config("POSTGRES_ENGINE"),
        "NAME": config("PGDATABASE"),
        "USER": config("PGUSER"),
        "PASSWORD": config("PGPASSWORD"),
        "HOST": config("PGHOST"),
        "PORT": config("PGPORT"),
    },
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # noqa
    },
]


LANGUAGE_CODE = "pt-BR"

TIME_ZONE = "America/Manaus"

USE_I18N = False  # se não for traduzir, melhor desativar

USE_TZ = True

DATE_FORMAT = "d/m/Y"

DATETIME_FORMAT = "d, M, Y - P"

DATETIME_INPUT_FORMATS = "d/m/Y H:i"

TIME_FORMAT = "G:i"

USE_THOUSAND_SEPARATOR = True

STATICFILES_DIRS = [
    BASE_DIR / "staticfiles",
]

STATIC_URL = "/static/static/"
MEDIA_URL = "/static/media/"

MEDIA_ROOT = BASE_DIR / "media"
STATIC_ROOT = BASE_DIR / "static"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CRISPY_TEMPLATE_PACK = "bootstrap4"

SITE_ID = 1

AUTH_USER_MODEL = "users.User"

AUTHENTICATION_BACKENDS = [
    # "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
]

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.ScryptPasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

LOGIN_URL = "users:login"

LOGOUT_REDIRECT_URL = "users:login"

ACCOUNT_SESSION_REMEMBER = True

# Só precisa digitar a senha uma vez
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
# Não precisa de username
ACCOUNT_USERNAME_REQUIRED = False
# Método de autenticação: email
ACCOUNT_AUTHENTICATION_METHOD = "email"
# Email obrigatório
ACCOUNT_EMAIL_REQUIRED = True
# Email único
ACCOUNT_UNIQUE_EMAIL = True
# Redicerionamento apos o cadastro
ACCOUNT_SIGNUP_REDIRECT_URL = "core:dashboard"

PORTIFOLIO_HOST = config("PORTIFOLIO_HOST")

WHATSAPP_URL = config("WHATSAPP_URL")

WHATSAPP_TOKEN = config("WHATSAPP_TOKEN")

WHATSAPP_TOKEN_PERMANENT = config("WHATSAPP_TOKEN_PERMANENT")

TOKEN_WEBHOOK = config("TOKEN_WEBHOOK")
