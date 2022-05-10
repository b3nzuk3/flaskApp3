from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app= Flask(__name__)

app.config['SECRET_KEY'] = '5c6b8cd67af797b778498e02f5619ef3'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


from flaskblog import routes
