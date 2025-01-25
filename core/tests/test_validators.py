from django.test import TestCase
from django.core.exceptions import ValidationError
from core.validators import validate_phone_number, validate_zip_code


class PhoneNumberValidatorTests(TestCase):
    def test_valid_phone_numbers(self):
        """Test that valid phone numbers pass validation."""
        valid_numbers = ["1234567890", "+11234567890"]
        for number in valid_numbers:
            validate_phone_number(number)  # Should not raise an exception

    def test_invalid_phone_numbers(self):
        """Test that invalid phone numbers raise a ValidationError."""
        invalid_numbers = ["12345", "abcd123456", "+123456789", "123-456-7890"]
        for number in invalid_numbers:
            with self.assertRaises(ValidationError):
                validate_phone_number(number)


class ZipCodeValidatorTests(TestCase):
    def test_valid_zip_codes(self):
        """Test that valid ZIP codes pass validation."""
        valid_zip_codes = ["12345", "12345-6789"]
        for zip_code in valid_zip_codes:
            validate_zip_code(zip_code)  # Should not raise an exception

    def test_invalid_zip_codes(self):
        """Test that invalid ZIP codes raise a ValidationError."""
        invalid_zip_codes = ["1234", "123456", "12-345", "12345-67890"]
        for zip_code in invalid_zip_codes:
            with self.assertRaises(ValidationError):
                validate_zip_code(zip_code)
