class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost/seashell_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your-secret-key-here'
