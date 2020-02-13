REQUIRED_CREATE_USER_DATA_KEYS = ("username", "email", "passwordHash")
REQUIRED_AUTH_DATA_KEYS = ("login", "passwordHash")


# validate_... functions
# return False, message if there is a error in validating

def validate_create_user_data(json):
    if not all(k in REQUIRED_CREATE_USER_DATA_KEYS for k in json):
        return False
    ...
    return True


def validate_auth_data(json):
    if not all(k in REQUIRED_AUTH_DATA_KEYS for k in json):
        return False
    ...
    return True