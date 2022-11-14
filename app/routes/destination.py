from app import app
from flask import render_template

def destination():
    return render_template('pages/destination.html')