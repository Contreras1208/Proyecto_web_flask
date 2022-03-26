from app import app

from db.db import landingdb

#from utils.db import db

with app.app_context():
    landingdb.create_all()

if __name__ == "__main__":
    app.run(debug=True)
    

