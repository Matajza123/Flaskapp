from flaskapp import app
from flask import render_template

@app.errorhandler(400)
def bad_request(e):
    return render_template('error.html', error = e)   

@app.errorhandler(403)
def forbidden(e):
    return render_template('error.html', error = e)  

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error = e)   

@app.errorhandler(405)
def method_not_allowed(e):
    return render_template('error.html', error = e) 

@app.errorhandler(500)
def server_error(e):
    return render_template('error.html', error = e)   