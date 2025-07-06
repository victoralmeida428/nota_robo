import os

from Service.singleton import SingletonMeta
from dotenv import load_dotenv
load_dotenv()

class AuthService(metaclass=SingletonMeta):
    __secret = os.getenv("PASSWORD", "")

    def __init__(self):
        self.__valid()

    def __valid(self):
        if self.__secret == "":
            raise EnvironmentError("Secret not set")

    def authenticate(self, password):
        if password != self.__secret:
            raise ValueError("Invalid password")