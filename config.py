import os

basedir = os.path.abspath(os.path.dirname(__file__)) # get the path of the current file

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') # get the secret key from the environment variable
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')\
        or 'sqlite:///' + os.path.join(basedir, 'app.db') # get the database url from the environment variable, or use the default sqlite database
    SQLALCHEMY_TRACK_MODIFICATIONS = False # disable the modification tracker for the database
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER') or "./uploads" # get the upload folder from the environment variable, or use the default uploads folder
    DOWNLOAD_FOLDER = os.environ.get('DOWNLOAD_FOLDER') or "./downloads" # get the download folder from the environment variable, or use the default downloads folder