from django.db import models
from django.contrib.auth.models import User

# Create your models here.
"""
Tables :
    
    1. User     ==> for store user's information

"""


class ResearcherUser(models.Model):

    """
    column :

        1. username
        2. name
        3. last name
        4. email
        5. phone number

    relation :

        1. User     :   one_to_one

    """

    # username
    username = models.CharField(max_length=25)

    # name
    name = models.CharField(max_length=25)

    # last name
    last_name = models.CharField(max_length=25)

    # email
    user_email = models.EmailField()

    # phone number
    phone_number = models.CharField(max_length=15)

    # relation
    user = models.OneToOneField(User, on_delete=models.CASCADE)
