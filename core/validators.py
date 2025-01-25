import re
from django.core.exceptions import ValidationError


def validate_phone_number(value):
    """
    Validates phone numbers in one of the following formats:
    - 10-digit numbers (e.g., 1234567890).
    - International numbers starting with +1 (e.g., +11234567890).
    """
    if not re.match(r"^(\+1\d{10}|\d{10})$", value):
        raise ValidationError(
            "Enter a valid phone number (10 digits or +11234567890 format)."
        )

    return value


def validate_zip_code(value):
    """
    Validates ZIP codes in the following formats:
    - 5-digit ZIP codes (e.g., 12345).
    - 9-digit ZIP codes with a dash (e.g., 12345-6789).
    """
    if not re.match(r"^\d{5}(-\d{4})?$", value):
        raise ValidationError("Enter a valid ZIP code (e.g., 12345 or 12345-6789).")
    return value
