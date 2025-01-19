from flask import Flask

app= Flask(__name__)


@app.route("/")
def home():
    print("dfsdfdsfsdfsdfdsfdsdf")



@app.route("/working")
def woking():
    print("dkfjsldkfjldskf")



@app.route("/register")
def register():
    print("register views")
    

@app.route("/logout")
def logout():
    print("logout view")

if __name__=="__main__":
    app.run()