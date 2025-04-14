from flask import Flask
from .config import Config


from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://lab5user:reyboss123@localhost/lab5'
app.config['UPLOAD_FOLDER'] = 'uploads'  # Add if not already
app.config['SECRET_KEY'] = 'super-secret-key'  # Needed for CSRF

db = SQLAlchemy(app)
migrate = Migrate(app, db)
csrf = CSRFProtect(app)

from .views import views
app.register_blueprint(views)

