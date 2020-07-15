from flask import session, redirect, url_for
from functools import wraps


def login_required(route):
	'''Checks for presence of `\'user\'` in session cookie. If nonexistant, redirects to login page'''

	@wraps(route)
	def wrapper(*args, **kwargs):
		if 'user' in session:
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
