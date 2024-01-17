import subprocess
from flask import Flask
app = Flask(__name__)
app.debug = True

@app.route("/Update")
def updateCheck():
    # IF Change in github repo
    subprocess.run(['git fetch'])
    subprocess.run(['git pull'])
    subprocess.run(['sudo bash Buildfile'])
