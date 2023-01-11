from flask import *
from .utils import dbctrl as db
from .utils import decorators as dec 
from os import urandom, getenv
import hashlib
import random
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)


app.secret_key = getenv("FLASKSECRET")



@app.route("/", methods=['GET'])
@dec.login_required
def index():
	if "user" in session:
		return render_template("home.html")
	return redirect(url_for("login"))


@app.route("/login", methods=['GET', 'POST'])
# @dec.force_logout
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
		newuser = db.UserInfo(username=username, hashed_password=hashedpassword, salt=salt, rank="user").save()
		session["user"] = username
		return redirect(url_for("index"))
	return render_template("register.html")


@app.route("/characters", methods=["GET", "POST"], strict_slashes=False)
@dec.login_required
def characters():
	if request.method == "GET":
		allchars = db.UserInfo.objects(username=session["user"])[0].allcharacters
		return render_template("characters.html", characters=allchars)
	inputs = request.form.to_dict()
	print(inputs)
	if inputs["name"].isspace() or inputs["class"].isspace() or (len(inputs["class"]) == 0) or (len(inputs["name"]) == 0):
		flash("characters must have a name and a class", "warning")
		return redirect(url_for("characters"))
	users = db.UserInfo.objects(username=session["user"])
	user = users[0]
	c = int(random.random() * 100000000000000)
	newc = db.Character(name = inputs["name"], ptype=inputs["class"], charid=c, description=inputs["description"]).save()
	user.allcharacters.append(newc)
	user.save()
	return redirect(url_for("characters"))


@app.route("/characters/<int:charid>/view", methods=["GET", "POST"])
@dec.login_required
@dec.charownershipcheck
def viewcharacter(charid):
	if request.method == "GET":
		char = db.Character.objects(charid = charid)[0]
		return render_template("singlechar.html", char = char)
	
	inputs = request.form.to_dict()
	# print(inputs)
	char = db.Character.objects(charid=charid)[0]
	itemid = int(random.random() * 100000000000000000)
	tagso = []
	for x in inputs.keys():
		if "tag" in x:
			tagso.append(x[4:])
	newi = db.Item(name=inputs["name"], description=inputs["description"], itemid = itemid, tags = tagso)
	char.inventory.append(newi)
	char.save()
	return redirect(url_for("viewcharacter", charid = charid))

@app.route("/characters/<int:charid>/update", methods=["POST"])
@dec.login_required
@dec.charownershipcheck
def updatechar(charid):
	inputs = request.form.to_dict()
	char = db.Character.objects(charid=charid)[0]
	char.name = inputs["name"]
	char.ptype = inputs["class"]
	char.description = inputs["description"]
	char.save()
	return redirect(url_for("viewcharacter", charid = charid))
	pass

@app.route("/characters/<int:charid>/updateitem", methods=["POST"])
@dec.login_required
@dec.charownershipcheck
def updateitem(charid):
	inputs = request.form.to_dict()
	char = db.Character.objects(charid = charid)[0]
	for x in char.inventory:
		if x.itemid == int(inputs["itemid"]):
			x.name = inputs["itemname"]
			x.description = inputs["description"]
			char.save()
	return redirect(url_for("viewcharacter", charid = charid))
	pass


@app.route("/characters/<int:charid>/deleteitem", methods=["POST"])
@dec.login_required
@dec.charownershipcheck
def deleteitem(charid):
	inputs = request.form.to_dict()
	char = db.Character.objects(charid=charid)[0]
	for x in char.inventory:
		if x.itemid == int(inputs["itemid"]):
			print("here")
			char.inventory.remove(x)
			# x.delete()
			char.save()
	return redirect(url_for("viewcharacter", charid=charid))
	pass

@app.route("/characters/<int:charid>/delete", methods=["POST"])
@dec.charownershipcheck
def deletechar(charid):
	inputs = request.form.to_dict()
	char = db.Character.objects(charid = charid)[0].pk
	db.Character.objects(charid=charid)[0].delete()

	user = db.UserInfo.objects(username=session["user"]).update_one(pull__allcharacters=char)
	print(char)
		
	# 	print(x.charid)
	return redirect(url_for("characters"))
	# return inputs
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


@app.route("/characters/<int:charid>/rollers", methods=["GET"])
@dec.login_required
def rollers(charid):
	char = db.Character.objects(charid=charid)[0]
	return render_template("roller.html", char = char)
	pass


@app.route("/characters/<int:charid>/rollers/new", methods=["POST"])
@dec.login_required
@dec.charownershipcheck
@dec.diceverify
def newroller(charid):
	inputs = request.form.to_dict()
	rollerid = int(random.random() * 100000000000000000)
	darray = inputs["alldice"].split(",")
	rollerdice = []
	print(inputs["sign"] + inputs["modifier"])
	modifier = int(inputs["sign"] + inputs["modifier"])
	for n, x in enumerate(darray[::2]):
		realpos = n*2
		spos = realpos + 1
		d = db.Dice(n=int(x.split("_")[1]), s=int(darray[spos].split("_")[1]))
		rollerdice.append(d)
		pass

	r = db.Roller(name=inputs["name"], rollerid=rollerid, modifier=modifier, dice=rollerdice)

	char = db.Character.objects(charid=charid)[0]
	char.rollers.append(r)
	char.save()

	# return inputs
	return redirect(url_for('rollers', charid = charid))


@app.route("/characters/<int:charid>/rollers/delete", methods=["POST"])
@dec.login_required
@dec.charownershipcheck
def deleteroller(charid):
	inputs = request.form.to_dict()
	char = db.Character.objects(charid=charid)[0]
	for roller in char.rollers:
		if roller.rollerid == int(inputs["rollerid"]):
			print("HERE")
			char.rollers.remove(roller)
			char.save()
	return redirect(url_for("rollers", charid=charid))

@app.route("/help", methods=["GET"])
def help():
	return render_template("help.html")	
	pass


@app.route("/debug")
def deb():

	return render_template("debug.html")

if __name__ == "__main__":
	app.run(host="0.0.0.0", port="8082")
