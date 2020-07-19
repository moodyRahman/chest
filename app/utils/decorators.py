from flask import session, redirect, url_for, request, flash
from functools import wraps
import app.utils.dbctrl as db


def login_required(route):
	'''Checks for presence of `\'user\'` in session cookie. If nonexistant, redirects to login page'''

	@wraps(route)
	def wrapper(*args, **kwargs):
		if 'user' in session:
			if len(db.UserInfo.objects(username=session["user"])) == 0:
				session.pop("user")
				return redirect(url_for("login"))
			else:
				return route(*args, **kwargs)
		else:
			return redirect(url_for('login'))	
	return wrapper


def force_logout(route):
	'''Removes `\'user\'` from session cookie'''

	@wraps(route)
	def wrapper(*args, **kwargs):
		session.pop('user', None)
		return route(*args, **kwargs)

	return wrapper

def charownershipcheck(route):
	@wraps(route)
	def wrapper(*args, **kwargs):
		if request.method == "POST":
			inputs = request.form.to_dict()
			user = db.UserInfo.objects(username = session["user"])[0]
			inputcharid = int(inputs["charid"])
			if inputcharid in [x.charid for x in user.allcharacters]:
				print("THE USER IS VERIFIED")
				return route(*args, **kwargs)
			else:
				flash("you're not verified fool")
				return redirect(url_for("login"))
		else:
			return route(*args, **kwargs)
	
	return wrapper
