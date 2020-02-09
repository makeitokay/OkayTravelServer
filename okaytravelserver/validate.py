REQUIRED_CREATE_USER_DATA_KEYS = ("username", "email", "passwordHash")

REQUIRED_SYNC_DATA_KEYS = ("user")
REQUIRED_SYNC_USER_KEYS = ("user", "trips")
REQUIRED_SYNC_USER_INFO_KEYS = (
    "username",
    "email",
    "passwordHash",
    "avatar",
    "lastUpdateDatetime",
)
REQUIRED_SYNC_TRIPS_KEYS = ("trip", "budget", "places")
REQUIRED_SYNC_TRIP_KEYS = ("ownPlace", "startDate", "duration")
REQUIRED_SYNC_BUDGET_KEYS = ("amount", "category")
REQUIRED_SYNC_PLACE_KEYS = ("name", "date")

REQUIRED_AUTH_DATA_KEYS = ("login", "passwordHash")


# validate_... functions
# return False, message if there is a error in validating

def validate_create_user_data(json):
    if not all(k in REQUIRED_CREATE_USER_DATA_KEYS for k in json):
        return False
    ...
    return True


def validate_sync_data(json):
    if not all(k in REQUIRED_SYNC_DATA_KEYS for k in json):
        return False
    if not all(k in REQUIRED_SYNC_USER_KEYS for k in json["user"]):
        return False
    if not all(k in REQUIRED_SYNC_USER_INFO_KEYS for k in json["user"]["user"]):
        return False
    # for trip in json["user"]["trips"]:
    #     if not all(k in REQUIRED_SYNC_TRIPS_KEYS for k in trip):
    #         return False
    #     for budget_el in trip["budget"]:
    #         if not all(k in REQUIRED_SYNC_BUDGET_KEYS for k in budget_el):
    #             return False
    #     for place in trip["places"]:
    #         if not all(k in REQUIRED_SYNC_PLACE_KEYS for k in place):
    #             return False
    return True


def validate_auth_data(json):
    if not all(k in REQUIRED_AUTH_DATA_KEYS for k in json):
        return False
    ...
    return True