#!/usr/bin/env python3
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # user_id = models.IntegerField()
    bio = models.TextField(blank=True)
    Profile_img = models.ImageField(
        upload_to='profile_images%y%m%d', default='book-icon.png')
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username


if __name__ == "__main__":
    user0 = User()
    user1 = User(name="kapaka", age=25)
    print(f"user0.__dict__ {user0.__dict__}")
    print(f"user1.__dict__ {user0.__dict__}")
