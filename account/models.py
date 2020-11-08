from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):
    def create_user(self, id, name, email, department, password):
        if not id and name and email and department and password:
            raise ValueError(_('Users must have all field'))

        user = self.model(
            id=id,
            name=name,
            email=self.normalize_email(email),
            department=department
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, id, name, email, department, password):
        user = self.create_user(id, name, email, department, password)
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    id = models.CharField(
        verbose_name=_('id'),
        max_length=20,
        unique=True,
        primary_key=True
    )
    name = models.CharField(
        verbose_name=_('name'),
        max_length=50,
        unique=True
    )
    email = models.EmailField(
        verbose_name=_("email"),
        max_length=30,
        unique=True
    )
    department = models.CharField(
        verbose_name=_('department'),
        max_length=20,
    )
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'id'
    REQUIRED_FIELDS = ['name', 'email', 'department']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return self.id

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_username(self):
        return self.name

    def get_user_department(self):
        return self.department

    def get_user_email(self):
        return self.email

    @property
    def is_staff(self):
        return self.is_superuser