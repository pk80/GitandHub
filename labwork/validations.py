#!/usr/bin/env python3

import re


def validate_user(username, min_len):
    """Checks if the received username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if min_len < 1:
        raise ValueError("min_len must be at least 1")

    # Usernames can't be shorter than min_len
    if len(username) < min_len:
        return False
    # Usernames can only use letters, numbers, dots and underscores
    if not re.match('^[a-z0-9._]*$', username):
        return False
    # Usernames can't begin with a number
    if username[0].isnumeric():
        return False
    return True


print(validate_user("blue.kale", 3))  # True
print(validate_user(".blue.kale", 3))  # Currently True, should be False
print(validate_user("red_quinoa", 4))  # True
print(validate_user("_red_quinoa", 4))  # Currently True, should be False

# COMMENTS
# Here, as we see the output, it function returns true
# even if the username doesn't start with a letter.
# Here we need to change the check of the first character
# as only letters are allowed in the first character of the username.
