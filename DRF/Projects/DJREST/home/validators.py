# Custom validator
from rest_framework.validators import ValidationError

def no_numbers(value):
    if any(char.isdigit() for char in value):
        return ValidationError("name should not contain numbers")
    