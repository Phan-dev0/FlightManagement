from app import app
from flask import render_template

def register():
    return render_template('pages/register.html')
