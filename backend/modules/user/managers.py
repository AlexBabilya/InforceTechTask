from django.contrib.auth.models import BaseUserManager

from modules.role.models import Role


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **kwargs):
        """
        Create and return a `User` with an email, phone number, username and password.
        """

        if username is None:
            raise TypeError("Users must have a username.")
        if email is None:
            raise TypeError("Users must have an email.")
        if password is None:
            raise TypeError("User must have an password.")
        print(kwargs)
        role_group, _ = Role.objects.get_or_create(name=kwargs.get("roles")[0]["name"])

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=kwargs.get("first_name").capitalize(),
            last_name=kwargs.get("last_name").capitalize(),
            is_active=True,
            phone=kwargs.get("phone"),
            identification_no=kwargs.get("identification_no"),
        )

        user.set_password(password)
        user.save(using=self._db)
        user.roles.add(role_group)
        return user

    def create_stuff(self, username, email, password=None, **kwargs):
        """
        Create and return a `User` with staff permissions.
        """

        user = self.create_user(username, email, password, **kwargs)

        user.is_staff = True
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password, **kwargs):
        """
        Create and return a `User` with superuser (admin) permissions.
        """

        user = self.create_stuff(username, email, password, **kwargs)
        user.is_superuser = True
        user.save(using=self._db)

        return user
