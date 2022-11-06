import re
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import UserData


# For User Name Validation
def user_validation(val):
    UserName = UserData.objects.all()
    if UserName:
        for data in UserName:
            print(data.user_name)
            if data.user_name == val:
                raise ValidationError("User already exists...")
    else:
        print("New user add successfully...")
        return val


# For User Password Validation
def pass_validate(val):
    if re.match(r"^(?=[^A-Z]*[A-Z])(?=[^0-9]*[0-9])", val):
        return val
    else:
        raise ValidationError("Enter a valid password...")


class UserSerializer(serializers.ModelSerializer):
    """Validate some input details..."""
    password = serializers.CharField(validators=[pass_validate])
    user_name = serializers.CharField(validators=[user_validation])

    class Meta:
        model = UserData
        fields = "__all__"
