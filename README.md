# GRASP-WEB
Web Workflow for GRASP-HPO

## FLASK ENV FILE
You will need to create a .flaskenv file in the same directory as the config.py and supply it with arguments. 

Here is a sample version to get the app started.
```
FLASK_APP=app
FLASK_ENV=development
SECRET_KEY=verysecretkey
UPLOAD_FOLDER=app/uploads
DOWNLOAD_FOLDER=app/downloads
```
Once that is done, just use flask run in the GRASP-WEB folder.
