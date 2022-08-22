from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

ROLE_CHOICE = (
    (1, 'Admin'),
    (2, 'Oficial'),
    (3, 'Funcionário')
)

PERSON_TYPE_CHOICE = (
    (1, 'PF'),
    (2, 'PJ')
)

from .State import State
from .Authority import Authority
from .ReceivedOL import ReceivedOL
from .SentOL import SentOL
