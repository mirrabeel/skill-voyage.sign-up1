from flask import Flask
from flask_mail import Mail
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)  # გადოტვირთავს კონფიგურაციებს config.py-დან

db = SQLAlchemy(app)   # SQLAlchemy-ის ობიექტი, რომელიც გამოიყენება მონაცემთა ბაზასთან მუშაობისთვის
mail = Mail(app)       # Mail-ის ობიექტი, რომელიც გამოიყენება ელ. ფოსტის გაგზავნისთვის Flask აპლიკაციიდან


