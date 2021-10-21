# Backend

## Setting up Virtual Environment for Flask

Steps:

1. Set your current directory to the folder named `Image-upload-API` in powershell or vscode terminal
1. Type `python -m venv venv` in the terminal
1. After installing the necessities type `.\venv\Scripts\activate` to activate the venv. On Linux/Mac machines it will be `source venv/bin/activate.sh`
1. A venv folder should be created, now to install the requirements type `pip install -r .\requirements.txt` in the same terminal
1. Now that the Virtual Environment is activated you should reset your directory back to `image-classifier-example`
1. To run the Flask app, run `python backend/Image-upload-API/flask-api/main.py`
1. To exit the virtual environment simply type `deactivate` in the terminal
