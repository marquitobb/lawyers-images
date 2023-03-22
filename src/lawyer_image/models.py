import os
import pymysql
from dotenv import load_dotenv

load_dotenv()

class LawyerImageModel:
    def __init__(self):
        self.connection = pymysql.connect(
            host=os.environ.get('HOST'),
            user=os.environ.get('USER_HOST'),
            password=os.environ.get('PASSWORD_HOST'),
            db=os.environ.get('DB_HOST'),
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor)

    def get_all_lawyer_images(self):
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM lawyer_images"
            cursor.execute(sql)
            result = cursor. fetchall()
            return result