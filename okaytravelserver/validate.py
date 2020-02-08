REQUIRED_USER_DATA_KEYS = ("username", "email", "password_hash")


# validate_... functions
# return False, message if there is a error in validating

def validate_create_user_data(json):
    if not all(k in REQUIRED_USER_DATA_KEYS for k in json):
        return False
    return True