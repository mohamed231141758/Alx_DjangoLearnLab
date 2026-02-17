# Deployment Guide for Social Media API

## Prerequisites
- Git
- Python 3.8+
- PostgreSQL (for production)
- Heroku CLI (if deploying to Heroku)

## Local Setup
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## Production Deployment (Heroku)

### 1. Install Heroku CLI
```bash
curl https://cli-assets.heroku.com/install.sh | sh
```

### 2. Login to Heroku
```bash
heroku login
```

### 3. Create Heroku App
```bash
heroku create your-app-name
```

### 4. Add PostgreSQL
```bash
heroku addons:create heroku-postgresql:mini
```

### 5. Set Environment Variables
```bash
heroku config:set SECRET_KEY='your-secret-key'
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS='your-app-name.herokuapp.com'
```

### 6. Deploy
```bash
git push heroku main
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

### 7. Open App
```bash
heroku open
```

## Environment Variables Required
- `SECRET_KEY`: Django secret key
- `DEBUG`: Set to False in production
- `ALLOWED_HOSTS`: Your domain names
- `DATABASE_URL`: PostgreSQL connection string (auto-set by Heroku)
- `SECURE_SSL_REDIRECT`: True for HTTPS

## Monitoring
```bash
heroku logs --tail
```

## Maintenance
- Regular updates: `git push heroku main`
- Database backups: `heroku pg:backups:capture`
- View metrics: Heroku dashboard

## Security Checklist
- ✅ DEBUG = False
- ✅ SECRET_KEY in environment variable
- ✅ ALLOWED_HOSTS configured
- ✅ HTTPS enabled
- ✅ Security headers configured
- ✅ Database connection secured
