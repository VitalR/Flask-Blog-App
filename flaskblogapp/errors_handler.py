from flaskblogapp import app
from flask import render_template, request


@app.errorhandler(404)
def error_404(error):
    return render_template('404.html'), 404


@app.errorhandler(403)
def error_403(error):
    return render_template('403.html'), 403


@app.errorhandler(500)
def error_500(error):
    return render_template('500.html'), 500
