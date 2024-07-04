#!/bin/bash

# Fetch the signup page to get the CSRF token and cookie
response=$(curl -s -c cookies.txt http://127.0.0.1:8000/signup)
CSRF_TOKEN=$(echo "$response" | grep -o 'name="csrfmiddlewaretoken" value="[^"]*' | sed 's/name="csrfmiddlewaretoken" value="//')
echo "CSRF Token: $CSRF_TOKEN"  # Verify the token

# Make POST request with CSRF token and cookie
curl -X POST http://127.0.0.1:8000/api_signup \
  -b cookies.txt \
  -H "Content-Type: application/json" \
  -H "X-CSRFToken: $CSRF_TOKEN" \
  -d '{
    "username": "example0",
    "email": "example0@example.com",
    "password": "example0",
    "password2": "example0"
  }'
