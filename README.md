# Shorten-url-ids

This is an API that creates http service for shortening urls.

## A brief description

This project implements a simple and efficient URL shortener API built with FastAPI.

It handles:

- Structure project.

- URL shortening with a unique identifier (dealing with collisions)

- Validated input using Pydantic

- Auto database and table creation on the first app startup 

- Async interaction with SQLite database using SQLAlchemy

- Easy deployment using Docker.

## Technologies:

- Python 

- FastAPI

- Pydantic

- SQLAlchemy (asyncio)

- SQLite

- Docker

## Methods:

### *POST /*

The method accepts the URL string for shortening in the request body and returns a response of the short_url_id with the code 201 .

#### Example:

Request:

```json
{
  "url": "https://example.com"
}
```

Response:

```json
{
  "short_url": "a1234"
}
```

### *GET /<shorten-url-id>*

The method takes the identifier of the shortened URL as a parameter and returns a response with the code 307 and redirects to the original URL.

#### Example:

Request:

```
URL: http://127.0.0.1:8000/a1234
```

Response:

```
307 Temporary Redirect
Redirect to https://example.com
```


