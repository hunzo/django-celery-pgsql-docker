import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DB_USERNAME = os.environ.get("POSTGRES_USER")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
DB_DATABASE = os.environ.get("POSTGRES_DB")
DB_HOST = os.environ.get("POSTGRES_HOST")
DB_PORT = os.environ.get("POSTGRES_PORT")
DB_IS_AVAIL = all([
    DB_USERNAME,
    DB_PASSWORD,
    DB_DATABASE,
    DB_HOST,
    DB_PORT
])


DB_IGNORE_SSL = os.environ.get("DB_IGNORE_SSL") == "true"
# POSTGRES_READY=str(os.environ.get('POSTGRES_READY')) == "1"

print("init database: ")
print("-"*100)

print(
    DB_HOST,
    DB_USERNAME,
    DB_PASSWORD,
    DB_DATABASE,
    DB_PORT,
    DB_IS_AVAIL,
    DB_IGNORE_SSL,
    # POSTGRES_READY
    )

if DB_IS_AVAIL:
    print("Using Postgres")
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": DB_DATABASE,
            "USER": DB_USERNAME,
            "PASSWORD": DB_PASSWORD,
            "HOST": DB_HOST,
            "PORT": DB_PORT,
        }
    }
    if not DB_IGNORE_SSL:
        DATABASES["default"]["OPTIONS"] = {
            "sslmode": "require"
        }
else:
    print("Using SQLite")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db/db.sqlite3',
        }
    }

print("-"*100)
