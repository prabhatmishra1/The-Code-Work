from .models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserAdminCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('email',)


class UserAdminChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = User
        fields = ('email',)
