from django.contrib.auth.forms import UserCreationForm

from .models import User


class RegisterForm(UserCreationForm):
    # TODO 密码和验证密码属性定义在父类的属性中
    class Meta(UserCreationForm.Meta):
        # TODO 这里是拓展的User
        model = User
        fields = ("username", "email")
