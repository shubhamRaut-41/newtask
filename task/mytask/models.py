from django.db import models


# Create your models here.
class UserData(models.Model):
    """ User Data Models """
    user_name = models.CharField(max_length=25)
    email_id = models.EmailField()
    password = models.CharField(max_length=30)
    active = models.CharField(default=False, max_length=10)

    class Meta:
        db_table = "user-form"
