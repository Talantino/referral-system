# Referral-system

## Install and up backend

1. Install Docker and docker-compose.

For Debian, Ubuntu:

```
su
apt update; apt upgrade -y; apt install -y curl; curl -sSL https://get.docker.com/ | sh; curl -L https://github.com/docker/compose/releases/download/1.28.2/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose && chmod +x /usr/local/bin/docker-compose
```

Don't forget press CTRL+D to exit from super user account.

2. Apply environment variables and change .env file:

```
cp example.env .env
POSTGRES_HOST=postgres
REDIS_HOST=redis
```

3. Up docker-compose, migrate database and create super user:

```
docker-compose up --build
docker-compose exec backend bash
python manage.py createsuperuser
```

4. open project swagger

http://0.0.0.0:8000/api/docs/
