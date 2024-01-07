# read config file via this file
import configparser
import logging

config = configparser.RawConfigParser()
config.read('.\\configuration/config.ini')


# static method is used so that user do not have to create an object to
# call the class.We can directly call the class and it's functions.

class ReadConfig:
    @staticmethod
    def get_application_uRL():
        url = config.get('Common Info', 'baseurl')
        return url

    @staticmethod
    def user_email():
        user_name = config.get('Common Info', 'username')
        return user_name

    @staticmethod
    def user_password():
        user_password = config.get('Common Info', 'password')
        return user_password
