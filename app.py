from flask import Flask

app= Flask(__name__)


@app.route("/")
def home():
    print("dfsdfdsfsdfsdfdsfdsdf")



@app.route("/working")
def woking():
    print("dkfjsldkfjldskf")


if __name__=="__main__":
    app.run()