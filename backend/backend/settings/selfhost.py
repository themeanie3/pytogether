from .base import *
from decouple import config


DEBUG = False

DOMAIN = config("DOMAIN", default="")
USE_HTTPS = config("USE_HTTPS", default=False, cast=bool)

ALLOWED_HOSTS = [
    "django",
    "localhost",
    "127.0.0.1",
]

if DOMAIN:
    ALLOWED_HOSTS.append(DOMAIN)


SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SECURE_SSL_REDIRECT = USE_HTTPS

if USE_HTTPS:
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
else:
    SECURE_HSTS_SECONDS = 0

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

CSRF_COOKIE_SECURE = USE_HTTPS
SESSION_COOKIE_SECURE = USE_HTTPS


CSRF_TRUSTED_ORIGINS = []

CORS_ALLOWED_ORIGINS = []

if DOMAIN:
    CSRF_TRUSTED_ORIGINS += [
        f"http://{DOMAIN}",
        f"https://{DOMAIN}",
    ]

    CORS_ALLOWED_ORIGINS += [
        f"http://{DOMAIN}",
        f"https://{DOMAIN}",
    ]

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "OPTIONS",
    "DELETE",
    "PUT",
]

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

JWT_AUTH_COOKIE = "access_token"
JWT_AUTH_REFRESH_COOKIE = "refresh_token"
JWT_AUTH_SECURE = USE_HTTPS
JWT_AUTH_SAMESITE = "Lax"

REST_FRAMEWORK["DEFAULT_PERMISSION_CLASSES"] = (
    "rest_framework.permissions.IsAuthenticated",
)


STATIC_ROOT = BASE_DIR / "staticfiles"

# Email verification level: mandatory | optional | none (overridable for self-host)
ACCOUNT_EMAIL_VERIFICATION = config("ACCOUNT_EMAIL_VERIFICATION", default="mandatory")

# Email delivery. If EMAIL_HOST is set, use real SMTP; otherwise fall back to the
# console backend so verification emails are printed to the container logs.
EMAIL_HOST = config("EMAIL_HOST", default="")
if EMAIL_HOST:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_PORT = config("EMAIL_PORT", default=587, cast=int)
    EMAIL_HOST_USER = config("EMAIL_HOST_USER", default="")
    EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", default="")
    EMAIL_USE_TLS = config("EMAIL_USE_TLS", default=True, cast=bool)
    EMAIL_USE_SSL = config("EMAIL_USE_SSL", default=False, cast=bool)
else:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL", default="noreply@" + (DOMAIN or "localhost"))

AUTO_SAVE_INTERVAL = 60  # seconds
GHOST_CLEAN_INTERVAL = 600