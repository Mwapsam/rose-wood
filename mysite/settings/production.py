from .base import *

DEBUG = False

DEFAULT_FILE_STORAGE = "mysite.storage_backends.MediaRootS3Boto3Storage"
WAGTAILIMAGES_RENDITION_STORAGE = "mysite.storage_backends.MediaRootS3Boto3Storage"

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", "AKIA2UC3FNCUBINZYOJW")
AWS_SECRET_ACCESS_KEY = os.environ.get(
    "AWS_SECRET_ACCESS_KEY", "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"
)
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME", "rosegold-int")
AWS_DEFAULT_ACL = "public-read"
AWS_QUERYSTRING_AUTH = False

AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
AWS_LOCATION = "statics"


STATICFILES_STORAGE = "nkwazi_api.storage_backends.StaticRootS3Boto3Storage"
STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/{AWS_LOCATION}/"

MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, "")

