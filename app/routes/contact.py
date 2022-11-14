from app import app
from flask import render_template

def contact():
    return render_template('pages/contact.html')