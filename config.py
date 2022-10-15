from dotenv import load_dotenv
import os
load_dotenv()


SECRET_KEY = 'mgc1234'
SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{user}:{password}@{server}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        user = 'root',
        password = os.getenv('MY_SQL_PASSWORD'),
        server = 'localhost',
        database = 'my_game_collection'
    )

UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'