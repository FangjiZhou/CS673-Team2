# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


# Import a module / component using its blueprint handler variable (api_module)
from app.api_module.user_controllers import api_mod as api_mod
from app.api_module.company_controller import company_mod as comp_mod
from app.api_module.role_controller import role_mod as role_mod
from app.api_module.team_controller import team_mod as team_mod
from app.api_module.employee_controller import employee_mod as employee_mod

# Register blueprint(s)
app.register_blueprint(api_mod)
app.register_blueprint(comp_mod)
app.register_blueprint(role_mod)
app.register_blueprint(team_mod)
app.register_blueprint(employee_mod)
# app.register_blueprint(xyz_module)

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()

