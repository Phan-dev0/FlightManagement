import sys
sys.path.append("./")
from app import app
from flask import render_template, request
import routes


with app.app_context():
    app.add_url_rule('/', view_func=routes.index) 
    app.add_url_rule('/register.html', view_func=routes.register) 
    app.add_url_rule('/destination.html', view_func=routes.destination) 
    app.add_url_rule('/index.html', view_func=routes.index) 
    app.add_url_rule('/pricing.html', view_func=routes.pricing) 
    app.add_url_rule('/contact.html', view_func=routes.contact) 


 

  
if __name__ == "__main__":
    app.run()

