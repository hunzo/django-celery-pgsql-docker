import os

CELERY_BROKER_URL = os.environ.get(
    "CELERY_BROKER_URL", "amqp://guest:guest@localhost:5672"
    # "CELERY_BROKER_URL", "redis://localhost:6379"
)

CELERY_TIMEZONE = "Asia/Bangkok"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_RESULT_BACKEND = "django-db"
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True

print("init celery: ")
print("-"*100)
print(
    CELERY_BROKER_URL,
    CELERY_RESULT_BACKEND,
    CELERY_TIMEZONE,
    CELERY_TASK_TRACK_STARTED,
)

# Change Backend
# CELERY_RESULT_BACKEND = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379/0")


print("-"*100)