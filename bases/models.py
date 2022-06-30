from django.db import models
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


from .managers import UserManager

class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(_('Email'), max_length=254, unique=True)
    first_name = models.CharField(_('First Name'), max_length=30, blank=True)
    last_name = models.CharField(_('Last Name'), max_length=30, blank=True)
    is_staff = models.BooleanField(_('es staff'), default=False,
        help_text=_('Indica si el user puede iniciar sesión en admin '))
    is_active = models.BooleanField(_('activo'), default=True,
        help_text=_('Designa si este user debe ser tratado como activo'
                    'Deseleccione esto en lugar de eliminar cuentas.'))
    date_joined = models.DateTimeField(_('fecha registro'), default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_absolute_url(self):
        return "/users/%s" % urlquote(self.email)
    
    def get_full_name(self):
        full_name = "%s %s" % (self.first_name,self.last_name)
        return full_name.strip()
    
    def get_short_name(self):
        return self.first_name