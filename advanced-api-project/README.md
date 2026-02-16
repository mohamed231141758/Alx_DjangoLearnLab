# Advanced API Project

## Endpoints

| Method | URL | Description | Auth Required |
|--------|-----|-------------|---------------|
| GET    | /api/books/ | List all books | No |
| GET    | /api/books/<id>/ | Get a book | No |
| POST   | /api/books/create/ | Create a book | Yes |
| PUT    | /api/books/<id>/update/ | Update a book | Yes |
| DELETE | /api/books/<id>/delete/ | Delete a book | Yes |

## Authentication
Uses Token Authentication. Get a token via /api/token/
Then use: Authorization: Token <your_token>
