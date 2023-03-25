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

    def save_lawyer_image(self, id_lawyer, image_path):
        try:
            with self.connection.cursor() as cursor:
                # Construye la sentencia SQL de inserción
                sentencia = "INSERT INTO lawyer_images (id_lawyer, image_url) VALUES (%s, %s)"
                # Crea una tupla con los valores a insertar
                valores = (id_lawyer, image_path)
                # Ejecuta la sentencia SQL
                cursor.execute(sentencia, valores)
            self.connection.commit()

            # validate is success
            if cursor.rowcount == 1:
                return True
            return False
        finally:
            self.connection.close()


    def get_all_lawyer_images(self):
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM lawyer_images"
                cursor.execute(sql)
                result = cursor. fetchall()
                return result
        finally:
            # Cierra la conexión
            self.connection.close()