import re
from email_validator import validate_email, EmailNotValidError


def is_valid_email(email):
    try:
        validate_email(email, check_deliverability=False)
        return True
    except EmailNotValidError:
        return False


def is_strong_password(password):
    """
    Password must contain:
    - At least 8 characters
    - One uppercase letter
    - One lowercase letter
    - One digit
    - One special character
    """

    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$"

    return re.match(pattern, password) is not None