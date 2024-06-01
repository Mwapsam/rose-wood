from .base import *

DEBUG = False

SECRET_KEY = os.environ.get("SECRET_KEY", "your-secure-default-secret-key")

CSRF_TRUSTED_ORIGINS = ["https://rosegold-ent.com"]

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"

ALLOWED_HOSTS = ["rosegold-ent.com", "www.rosegold-ent.com"]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, "static"),
]

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

DATA_UPLOAD_MAX_MEMORY_SIZE = 100 * 1024 * 1024
FILE_UPLOAD_MAX_MEMORY_SIZE = 50 * 1024 * 1024
WAGTAILIMAGES_MAX_UPLOAD_SIZE = 50 * 1024 * 1024

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": os.path.join(BASE_DIR, "logs/mysite.log"),
        },
    },
    "root": {
        "handlers": ["file"],
        "level": "INFO",
    },
}
