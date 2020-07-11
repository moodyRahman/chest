from flask import *
from .utils import dbctrl as db
from os import urandom
import hashlib

app = Flask(__name__)

app.secret_key = "debug"


@app.route("/", methods=['GET'])
def index():
	if "user" in session:
		return render_template("home.html")
	return redirect(url_for("login"))


@app.route("/login", methods=['GET', 'POST'])
def login():
	if request.method == "POST":
		inputs = request.form.to_dict()
		users = db.UserInfo.objects(username=inputs["username"])
		if users:
			password = inputs["password"]
			salt = users[0]["salt"]
			hashedpasswordcalc = hashlib.sha512(
                            (password + salt).encode("utf-8")).digest().hex()
			if hashedpasswordcalc == users[0]["hashed_password"]:
				session["user"] = users[0]["username"]
				flash("sucessfully logged in")
				return redirect(url_for("index"))
			flash("incorrect password")
			return redirect(url_for("login"))
		else:
			flash("username not found")
			return redirect(url_for("login"))
	return render_template("login.html")


@app.route("/logout", methods=['POST', 'GET'])
def logout():
	session.pop("user")
	flash("successful log out")
	return redirect(url_for("login"))
	pass

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
		if users:
			flash("username already exists")
			return redirect(url_for("register"))
		print(users)
		salt = urandom(64).hex()
		
		hashedpassword = hashlib.sha512(
		(pw0 + salt).encode("utf-8")).digest().hex()
		newuser = db.UserInfo(username=username, hashed_password=hashedpassword, salt=salt).save()
		session["user"] = username
		return redirect(url_for("index"))
	return render_template("register.html")

@app.route("/debug")
def deb():
	return request.form

if __name__ == "__main__":
	app.run()
