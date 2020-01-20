from flaskapp import app
from flask import render_template, request
from flask_login import current_user
from flaskapp.functions import log

@app.errorhandler(400)
def bad_request(e):
    log(e, request.path, current_user.id)
    return render_template('error.html', error = e)   

@app.errorhandler(403)
def forbidden(e):
    log(e, request.path, current_user.id)
    return render_template('error.html', error = e)  

@app.errorhandler(404)
def page_not_found(e):
    log(e, request.path, current_user.id)
    return render_template('error.html', error = e)   

@app.errorhandler(405)
def method_not_allowed(e):
    log(e, request.path, current_user.id)
    return render_template('error.html', error = e) 

@app.errorhandler(500)
def server_error(e):
    log(e, request.path, current_user.id)
    return render_template('error.html', error = e)   