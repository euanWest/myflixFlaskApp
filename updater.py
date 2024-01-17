import subprocess
from flask import Flask
# app = Flask(__name__)
# app.debug = True

# if __name__ == '__main__':
#     app.run(debug=True, port=80)

# instance of flask application
app = Flask(__name__)

@app.route("/Update")
def updateCheck():
   
    subprocess.run(['git fetch'])
    subprocess.run(['git pull'])
    subprocess.run(['sudo bash Buildfile'])

     # IF Change in github repo
    return "<p> Updating sever</p>"

 

 
# home route that returns below text 
# when root url is accessed
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
 
if __name__ == '__app__':
    app.run(debug=True, port=8001)