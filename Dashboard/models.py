from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)


# Make CustomUserManeger
class CustomUserManager(BaseUserManager):

    # Make a Function for Create Normal User
    def create_user(
        self,
        email=None,
        username=None,
        password=None,
        type_user="normal",
        firstname=None,
        lastname=None,
        **extra_fields,
    ):

        if not email:
            raise ValueError("The Email field must be set")
        elif not username:
            raise ValueError("The Username field must be set")
        elif not password:
            raise ValueError("The Password field must be set")
        elif not firstname:
            raise ValueError("The FirstName field must be set")
        elif not lastname:
            raise ValueError("The LastName field must be set")

        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            type_user=type_user,
            firstname=firstname,
            lastname=lastname,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    # Make a function for Create Seller User
    def create_seller(
        self,
        email=None,
        username=None,
        password=None,
        type_user="seller",
        firstname=None,
        lastname=None,
        store_name=None,
        store_description=None,
        **extra_fields,
    ):

        if not email:
            raise ValueError("The Email field must be set")
        elif not username:
            raise ValueError("The Username field must be set")
        elif not password:
            raise ValueError("The Password field must be set")
        elif not firstname:
            raise ValueError("The FirstName field must be set")
        elif not lastname:
            raise ValueError("The LastName field must be set")
        elif not store_name:
            raise ValueError("The NameOfStore field must be set")
        elif not store_description:
            raise ValueError("The DescriptionOfStore field must be set")

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            type_user=type_user,
            username=username,
            firstname=firstname,
            lastname=lastname,
            store_name=store_name,
            store_description=store_description,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    # Make a function for Create Admin User
    def create_admin(
        self,
        email=None,
        username=None,
        password=None,
        type_user="admin",
        firstname=None,
        lastname=None,
        **extra_fields,
    ):

        if not email:
            raise ValueError("The Email field must be set")
        elif not username:
            raise ValueError("The Username field must be set")
        elif not password:
            raise ValueError("The Password field must be set")
        elif not firstname:
            raise ValueError("The FirstName field must be set")
        elif not lastname:
            raise ValueError("The LastName field must be set")

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            type_user=type_user,
            firstname=firstname,
            lastname=lastname,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = [
        ("normal", "Normal User"),
        ("seller", "Seller User"),
        ("admin", "Admin User"),
    ]
    type_user = models.CharField(
        max_length=15, choices=USER_TYPE_CHOICES, default="normal"
    )

    email = models.EmailField(unique=True, null=False, blank=False)
    username = models.CharField(unique=True, max_length=150, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    store_description = models.TextField(max_length=1000, blank=False, null=False)
    store_name = models.CharField(max_length=50, null=False, blank=False)
    firstname = models.CharField(max_length=50, null=False, blank=False)
    lastname = models.CharField(max_length=50, null=False, blank=False)
    fullname = f"{firstname} {lastname}"

    objects = CustomUserManager()

    USERNAME_FIELD = "username"

    def __str__(self):
        return f"{self.fullname}, id={self.id}"
