# apps/users/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy as _

ROLE_CHOICES = [
    ('Admin', 'Admin'),
    ('User', 'User'),
    ('Vendor', 'Vendor'),
    ('Manager', 'Manager'),
    ('Support', 'Support'),
    ('Guest', 'Guest'),
    # Add more roles as needed
]

class User(AbstractUser):
    # your extra fields
    email = models.EmailField(_('email address'), unique=True)

    # override only if you need custom behavior
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_('The groups this user belongs to.'),
        related_name='custom_user_set',           # ← unique reverse name
        related_query_name='custom_user'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='custom_user_permissions',   # ← unique reverse name
        related_query_name='custom_user_perm'
    )
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='User',
        help_text='Designates the user’s role in the system.',
    )

class Organization(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
