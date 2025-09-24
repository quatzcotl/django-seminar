from datetime import datetime

from django.utils import timezone
from django.core.exceptions import ValidationError


def datetime_in_future(value: datetime) -> None:
    """
    Erhebe ValidationError wenn Datetime in der
    Vergangenheit liegt.
    """
    if value <= timezone.now():
        raise ValidationError("Das Datum darf nicht in der Vergangenheit liegen!")
