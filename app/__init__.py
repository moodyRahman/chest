from flask import *
from .utils import dbctrl as db
from os import urandom
import hashlib

app = Flask(__name__)



@app.route("/")
def index():
	return "hewwo"

@app.route("/register", methods=['GET', 'POST'])
def register():
	return render_template("login.html")

@app.route("/registerauth", methods=["POST"])
def registerauth():
	print(request.form)
	salt = urandom(64).hex()
	username = request.form["username"]
	hashedpassword = hashlib.sha512((request.form["password0"] + salt).encode("utf-8")).digest().hex()
	print(username, salt, hashedpassword)
	newuser = db.UserInfo(username = username, hashed_password = hashedpassword, salt = salt).save()
	return "a"

@app.route("/registerauth/query", method="POST")
def userexists():
	users = db.UserInfo.objects(username = request.form["username"])
	pass

@app.route("/debug")
def deb():
	return request.form

if __name__ == "__main__":
	app.run()
