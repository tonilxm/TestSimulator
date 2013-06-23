"""
decorators.py

Decorators for URL handlers

"""

from functools import wraps
from flask import redirect, abort, session, url_for


def login_required(func):
    """Requires standard login credentials"""
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not session['username']:
            return redirect(url_for('login'))
        return func(*args, **kwargs)
    return decorated_view


def admin_required(func):
    """Requires admin credentials"""
    @wraps(func)
    def decorated_view(*args, **kwargs):
        if not session['admin']:
            abort(401)  # Unauthorized
        return func(*args, **kwargs)
    return decorated_view
