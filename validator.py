import re

def is_non_empty(value: str, field_name: str) -> str:
    if not value.strip():
        raise ValueError(f"{field_name} is required")
    return value

def is_alphabetic(value: str, field_name: str) -> str:
    if not re.match(r'^[a-zA-Z\s]+$', value):
        raise ValueError(f"{field_name} should only contain alphabets")
    return value

def validate_length(value: str, min_len: int, max_len: int, field_name: str) -> str:
    value_without_spaces = value.replace(" ", "")
    if len(value_without_spaces) < min_len:
        raise ValueError(f"{field_name} should be at least {min_len} characters")
    if len(value) > max_len:
        raise ValueError(f"{field_name} cannot be more than {max_len} characters")
    return value