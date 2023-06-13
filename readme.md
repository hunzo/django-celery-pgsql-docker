# django + celery + pgsql + docker

# verions
```
billiard==3.6.4.0
celery==5.2.7
kombu==5.2.4
```
## .envfile
```
DEBUG=1

DJANGO_ALLOWED_HOSTS=* localhost 127.0.0.1
DJANGO_SECRET_KEY=enter_your_django_secret_key
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_PASSWORD=admin
DJANGO_SUPERUSER_EMAIL=example@email.com

CSRF_TRUSTED_ORIGINS=http://localhost


POSTGRES_READY=0
POSTGRES_DB=djangoDB
POSTGRES_PASSWORD=pgPassword
POSTGRES_USER=pgUser
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

DB_IGNORE_SSL=true
DB_IS_AVAIL=True


CELERY_BROKER_URL=amqp://guest:guest@localhost:5672
```

## Diagram
```mermaid
graph LR
    C["Client"] --> N["nginx"]
    N --> D["django-app"]

    Ce["celery"] --> B["Broker"]
    D --> B
    subgraph app
        D
        Ce
    end
```

```bash
export POSGRES_READY=1
```

## start celery
```
celery -A core worker -l DEBUG
```
