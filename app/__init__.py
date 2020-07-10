from flask import *
from .utils import dbctrl as db
from os import urandom
import hashlib

app = Flask(__name__)

app.secret_key = "debug"

@app.route("/")
def index():
	return "hewwo"

@app.route("/register", methods=['GET', 'POST'])
def register():
	if request.method == "POST":
		print(request.form)
		inputs = request.form.to_dict()
		username = inputs["username"]
		pw0 = inputs["password0"]
		pw1 = inputs["password1"]
		if pw0 != pw1:
			flash("passwords have to match")
			return redirect(url_for("register"))
		if username == pw0:
			flash("username can't be the same as the password")
			return redirect(url_for("register"))
		users = db.UserInfo.objects(username = request.form["username"])
		if not users:
			flash("username already exists")
			return redirect(url_for("register"))
		print(users)
		return "a"
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

@app.route("/registerauth/query")
def userexists():
	# users = db.UserInfo.objects(username = request.form["username"])
	# if users:
	# 	return {"response":True}
	print(request.args)
	return {"response":False}
	pass

@app.route("/debug")
def deb():
	return request.form

if __name__ == "__main__":
	app.run()
