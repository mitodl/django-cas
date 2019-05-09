"CasTicketException, CasConfigException"
from __future__ import absolute_import
from django.core.exceptions import ValidationError

class CasTicketException(ValidationError):
    """The ticket fails to validate"""

class CasConfigException(ValidationError):
    """The config is wrong"""

