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

    def update_lawyer_image(self, id_lawyer, image_path):
        try:
            with self.connection.cursor() as cursor:
                # Actualizar los campos correspondientes de la tabla de abogados
                sql = "UPDATE lawyer_images SET image_url = %s WHERE id_lawyer = %s"
                cursor.execute(sql, (image_path, id_lawyer))
                self.connection.commit()  # Confirmar la actualización en la base de datos
                print("Se ha actualizado la imagen del abogado con id {}.".format(id_lawyer))
                return True
        except Exception as e:
            print("Error al actualizar la imagen del abogado: {}".format(str(e)))
            return False
        finally:
            self.connection.close()  # Cerrar la conexión con la base de datos


    def get_lawyer_images(self, id_lawyer):
        try:
            with self.connection.cursor() as cursor:
                sql = f"SELECT * FROM lawyer_images where id_lawyer={id_lawyer}"
                cursor.execute(sql)
                result = cursor. fetchall()
                return result
        finally:
            # Cierra la conexión
            self.connection.close()

    def delete_lawyer_image(self, id_lawyer) -> bool:
        try:
            with self.connection.cursor() as cursor:
                sql = f"DELETE FROM lawyer_images WHERE id_lawyer={id_lawyer}"
                cursor.execute(sql)
                self.connection.commit()
                print("Se ha eliminado la imagen del abogado con id {}.".format(id_lawyer))
                return True
        except Exception as e:
            print("Error al eliminar la imagen del abogado: {}". format(str(e)))
            return False
        finally:
            self.connection.close()