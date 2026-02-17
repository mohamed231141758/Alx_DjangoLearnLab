# Social Media API

## Setup
```bash
pip install django djangorestframework Pillow
python3 manage.py migrate
python3 manage.py runserver
```

## Endpoints

| Method | URL | Description | Auth |
|--------|-----|-------------|------|
| POST | /api/accounts/register/ | Register new user | No |
| POST | /api/accounts/login/ | Login and get token | No |
| GET/PUT | /api/accounts/profile/ | View/update profile | Yes |

## Authentication
Use Token Authentication:
`Authorization: Token <your_token>`

## Register Example
```json
POST /api/accounts/register/
{
    "username": "john",
    "email": "john@example.com",
    "password": "securepass123"
}
```

## Login Example
```json
POST /api/accounts/login/
{
    "username": "john",
    "password": "securepass123"
}
```
