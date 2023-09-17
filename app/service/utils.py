from functools import wraps
from flask import g, request, redirect, url_for

def roles_required(roles=None):
    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            if g.user is None:
                return redirect(url_for('/sem-permissao', next=request.url))
            return func(*args, **kwargs)
        return decorated_function
    return decorator