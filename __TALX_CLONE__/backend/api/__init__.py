#backend/api/__init__.py
from rest_framework import status
S200 = status.HTTP_200_OK
S201 = status.HTTP_201_CREATED
S304 = status.HTTP_304_NOT_MODIFIED
S400 = status.HTTP_400_BAD_REQUEST
S401 = status.HTTP_401_UNAUTHORIZED
S405 = status.HTTP_405_METHOD_NOT_ALLOWED
S404 = status.HTTP_404_NOT_FOUND