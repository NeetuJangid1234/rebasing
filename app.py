from flask import Flask

app= Flask(__name__)


@app.route("/")
def home():
    print("dfsdfdsfsdfsdfdsfdsdf")



@app.route("/working")
def woking():
    print("dkfjsldkfjldskf")


@app.route("/login")
def login():
    print("sdkfjldkfjlskdfjljdlkfjsdlk")