import base64


def encode_user_details(user_string):
    return base64.b64encode(user_string.encode('ascii'))


def decode_user_details(user_string):
    return base64.b64decode(user_string.decode('ascii'))
