from flask import *
from .utils import dbctrl as db
from .utils import decorators as dec 
from os import urandom, environ
import hashlib
import random

app = Flask(__name__)


if environ["chest_debug"] == "true":
	app.secret_key = "debug"
else:
	app.secret_key = urandom(32)



app.secret_key = "debug"

@app.route("/", methods=['GET'])
@dec.login_required
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
	c = int(random.random() * 100000000000000)
	newc = db.Character(name = inputs["name"], ptype=inputs["class"], charid=c).save()
	user.allcharacters.append(newc)
	user.save()
	return redirect(url_for("characters"))


@app.route("/characters/view/<int:charid>", methods=["GET", "POST"])
@dec.login_required
def viewcharacter(charid):
	if request.method == "GET":
		char = db.Character.objects(charid = charid)[0]
		return render_template("singlechar.html", char = char)
	
	inputs = request.form.to_dict()
	char = db.Character.objects(charid=charid)[0]
	itemid = int(random.random() * 100000000000000000)
	newi = db.Item(name=inputs["name"], description=inputs["description"], itemid = itemid)
	char.inventory.append(newi)
	char.save()
	return redirect(url_for("viewcharacter", charid = charid))


@app.route("/characters/update", methods=["POST"])
@dec.login_required
def updateitem():
	inputs = request.form.to_dict()
	char = db.Character.objects(charid = inputs["charid"])[0]
	for x in char.inventory:
		if x.itemid == int(inputs["itemid"]):
			x.name = inputs["itemname"]
			x.description = inputs["description"]
			char.save()
	return redirect(url_for("viewcharacter", charid = inputs["charid"]))
	pass

@app.route("/characters/delete", methods=["POST"])
@dec.login_required
def deleteitem():
	inputs = request.form.to_dict()
	char = db.Character.objects(charid=inputs["charid"])[0]
	for x in char.inventory:
		if x.itemid == int(inputs["itemid"]):
			print("here")
			char.inventory.remove(x)
			# x.delete()
			char.save()
	return redirect(url_for("viewcharacter", charid=inputs["charid"]))
	pass
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

	return render_template("debug.html")

if __name__ == "__main__":
	app.run()
