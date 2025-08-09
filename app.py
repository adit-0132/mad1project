from flask_sqlalchemy import SQLAlchemy
from flask import Flask,render_template
from backend.controllers import routes
from backend.models import db

def setup():
    app=Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///household.sqlite3"
    db.init_app(app)
    app.app_context().push()
    app.debug=True
    routes(app)
    print("success")
    return app

app=setup()

if __name__=="__main__":
    app.run()