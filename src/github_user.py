import requests
import src.utils as utils

class GithubUser:
    def __init__(self, user_name, password):
        self.username = user_name
        self.password = password
        print(self.username, self.password)

    @staticmethod
    def set_password(self):
        return input('Enter password ').replace('\n', ' ')



