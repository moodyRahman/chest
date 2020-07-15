from flask import *
from .utils import dbctrl as db
from .utils import decorators as dec 
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
@dec.force_logout
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
				flash("sucessfully logged in", "success")
				return redirect(url_for("index"))
			flash("incorrect password", "danger")
			return redirect(url_for("login"))
		else:
			flash("username not found", "primary")
			return redirect(url_for("login"))
	return render_template("login.html")


@app.route("/logout", methods=['POST', 'GET'])
def logout():
	session.pop("user")
	flash("successful log out", "success")
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
			flash("passwords have to match", "warning")
			return redirect(url_for("register"))
		if username == pw0:
			flash("username can't be the same as the password", "warning")
			return redirect(url_for("register"))
		users = db.UserInfo.objects(username = request.form["username"])
		if users:
			flash("username already exists", "warning")
			return redirect(url_for("register"))
		print(users)
		salt = urandom(64).hex()
		
		hashedpassword = hashlib.sha512(
		(pw0 + salt).encode("utf-8")).digest().hex()
		newuser = db.UserInfo(username=username, hashed_password=hashedpassword, salt=salt).save()
		session["user"] = username
		return redirect(url_for("index"))
	return render_template("register.html")

@app.route("/characters", methods=["GET", "POST"])
@dec.login_required
def characters():
	if request.method == "GET":
		allchars = db.UserInfo.objects(username=session["user"])[0].allcharacters
		return render_template("characters.html", characters=allchars)
	inputs = request.form.to_dict()
	users = db.UserInfo.objects(username=session["user"])
	user = users[0]
	c = len(user.allcharacters) + 1
	newc = db.Character(name = inputs["name"], ptype=inputs["class"], charid=c).save()
	user.allcharacters.append(newc)
	print(user.username)
	user.save()
	return redirect(url_for("characters"))


@app.route("/characters/view/<int:charid>", methods=["GET", "POST"])
@dec.login_required
def viewcharacter(charid):
	if request.method == "GET":
		user = db.UserInfo.objects(username=session["user"])[0]
		for x in user.allcharacters:
			if x.charid == charid:
				return render_template("singlechar.html", char = x)
				pass
			pass

		return redirect(url_for("characters"))
	
	user = db.UserInfo.objects(username=session["user"])[0]
	inputs = request.form.to_dict()
	for x in user.allcharacters:
		if x.charid == charid:
			newi = db.Item(name = inputs["name"], description=inputs["description"])
			x.inventory.append(newi)
			x.save()
			return render_template("singlechar.html", char=x)
		pass
	print("============")
	print(charid)
	return redirect(url_for("viewcharacter"))

@app.route("/campaigns", methods=["GET", "POST"])
@dec.login_required
def campaign():
	if request.method == "POST":
		inputs = request.form.to_dict()
		newc = db.Campaign(dm=session["user"], name = inputs["name"]).save()
		user = db.UserInfo.objects(username=session["user"])[0]
		user.allcampaigns.append(newc)
		user.save()
		return redirect(url_for("campaign"))
	campaign = db.UserInfo.objects(username=session["user"])[0].allcampaigns

	return render_template("campaigns.html", campaigns = campaign)

@app.route("/debug")
def deb():
	return request.form

if __name__ == "__main__":
	app.run()
