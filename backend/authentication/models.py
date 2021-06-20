import random
from django.db import models
from django.contrib.auth.models import AbstractUser
from . validators import phone_regix
from django.utils.translation import ugettext_lazy as _
from . managers import CustomUserManager
# Create your models here.


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    mobile = models.CharField(
        _('mobile'),
        validators=[phone_regix],
        max_length=10,
    )
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Code(models.Model):
    otp = models.CharField(max_length=5, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.otp

    def save(self, *args, **kwargs):
        number_list = [x for x in range(10)]
        code_items = []
        for i in range(5):
            num = random.choice(number_list)
            code_items.append(num)
        code_string = "".join(str(item) for item in code_items)
        self.otp = code_string
        return super().save(*args, **kwargs)
