import os

basedir = os.path.abspath(os.path.dirname(__file__)) # get the path of the current file

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') # get the secret key from the environment variable