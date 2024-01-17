import subprocess
from flask import Flask
app = Flask(__name__)
app.debug = True


@app.route("/Update")
def updateCheck():
   
    subprocess.run(['git fetch'])
    subprocess.run(['git pull'])
    subprocess.run(['sudo bash Buildfile'])

     # IF Change in github repo
    return "<p> Updating sever</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)