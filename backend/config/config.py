import os 

class Config:
    SQLALCHEMY_DATABASE_URI = (
        f"mysql+asyncmy://root:{os.environ.get('MYSQL_PASSWORD', 'root')}@localhost/seashell_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
