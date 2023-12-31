from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import click
from flask.cli import with_appcontext

app = Flask(__name__, static_url_path='/static')
app.config.from_object(Config);


db = SQLAlchemy(app)
migrate = Migrate(app, db)
Bcrypt = Bcrypt(app)
login  = LoginManager(app)
login.login_view='login'

from flaskr import controlDB, routes, models
from flaskr.models import CPU, CPUCooler

@app.cli.command('repop-db')
@with_appcontext
def repopulate_db_cmd():
    controlDB.reset_db(CPU)
    controlDB.reset_db(CPUCooler)
    controlDB.repopulate_db()
    click.echo('db repopulated')


