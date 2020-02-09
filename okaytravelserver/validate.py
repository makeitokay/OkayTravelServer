REQUIRED_USER_DATA_KEYS = ("username", "email", "password_hash")
REQUIRED_SYNC_DATA_KEYS = ("last_update_date", "username")
REQUIRED_AUTH_DATA_KEYS = ("login", "password_hash")


# validate_... functions
# return False, message if there is a error in validating

def validate_create_user_data(json):
    if not all(k in REQUIRED_USER_DATA_KEYS for k in json):
        return False
    ...
    return True


def validate_sync_data(json):
    if not all(k in REQUIRED_SYNC_DATA_KEYS for k in json):
        return False
    ...
    return True


def validate_auth_data(json):
    if not all(k in REQUIRED_AUTH_DATA_KEYS for k in json):
        return False
    ...
    return True