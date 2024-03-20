from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>sveiki</h1>"

if __name__=='__main__':
    app.run(port = 5000)

print("sveiki")