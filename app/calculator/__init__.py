from flask import Blueprint


#creating an instance of Blueprint class
main=Blueprint('main',__name__,template_folder='templates')

from app.calculator import routes,models