from flask import session, redirect, url_for
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