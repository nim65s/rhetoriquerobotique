# rhetoriquerobotique

## Dev

```
echo "
SECRET_KEY=$(openssl rand -base64 32)
POSTGRES_PASSWORD=$(openssl rand -base64 32)
EMAIL_HOST_PASSWORD=........
DEBUG=True" >> .env
./manage.py migrate
./manage.py runserver
```

## Integration / Prod

Setup [proxyta.net](http://proxyta.net), and

```
echo DOMAIN_NAME=eu >> .env
echo DSN=...... >> .env
docker-compose up -d
```
