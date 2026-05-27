# Enterprise Flask External API Integration

## Features

- Flask REST API
- PostgreSQL
- Redis Cache
- JWT Authentication
- Gunicorn
- Nginx Reverse Proxy
- Docker Compose
- Third-party API Integration
- Production-ready Architecture

## Start Project

docker compose up --build

## Login

POST /api/external/login

{
  "username": "admin"
}

## API Endpoints

GET     /api/external/posts
GET     /api/external/posts/1
POST    /api/external/posts
PUT     /api/external/posts/1
PATCH   /api/external/posts/1
DELETE  /api/external/posts/1