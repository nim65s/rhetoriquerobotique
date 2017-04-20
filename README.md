# rhetoriquerobotique

```
vf new -p python3.6 rhetoriquerobotique
vf connect
pip install -U -r requirements.txt
```

```
sudo mkdir -p /etc/django/rhetoriquerobotique
echo pipo > /etc/django/rhetoriquerobotique/secret_key.txt
echo pipo > /etc/django/rhetoriquerobotique/email_password
```

```
./manage.py migrate
./manage.py runserver
```
