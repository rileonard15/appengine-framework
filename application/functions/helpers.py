import hashlib
import base64
import random
from config.settings import password_salt


# jsonize cookies
def get_cookies(raw_cookies):
    cookies = {}
    if raw_cookies:
        for cookie in raw_cookies.split("; "):
            result = str(cookie).split("=")
            name = result[0]
            value = result[1]
            cookies[name] = value.replace('"', '')
    return cookies


# hash strings
def hash_item(email, password):
    i = email + password + SETTINGS["password_salt"]
    return base64.b64encode(hashlib.sha1(i).digest())


# convert ID to int if int and string if string
def normalize_id(this_id):
    try:
        return int(this_id)
    except:
        return this_id


