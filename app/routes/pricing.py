from app import app
from flask import render_template

def pricing():
    return render_template('pages/pricing.html')
