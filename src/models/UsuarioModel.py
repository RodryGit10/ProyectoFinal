from database.db import get_connection
from .entities.Usuario import Usuario

class UsuarioModel():

    @classmethod
    def get_usuarios(self):
        try:
            connection = get_connection()
            usuarios=[]

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, ci, nombre, primer_ap, segundo_ap, fecha_nac FROM usuario ORDER BY nombre ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    usuario = Usuario(row[0], row[1], row[2], row[3], row[4], row[5])
                    usuarios.append(usuario.to_JSON())
            connection.close()
            return usuarios
        except Exception as ex:
            raise Exception(ex) 

    # Obtner datos    
    @classmethod
    def get_usuario(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, ci, nombre, primer_ap, segundo_ap, fecha_nac FROM usuario WHERE id = %s", (id,))
                row = cursor.fetchone()

                usuario = None
                if row != None:
                    usuario = Usuario(row[0], row[1], row[2], row[3], row[4], row[5])
                    usuario = usuario.to_JSON()
            connection.close()
            return usuario
        except Exception as ex:
            raise Exception(ex)

    # Agregar usuario    
    @classmethod
    def add_usuario(self, usuario):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO usuario (id, ci, nombre, primer_ap, segundo_ap, fecha_nac) 
                                VALUES (%s, %s, %s, %s, %s, %s)""", (usuario.id, usuario.ci, usuario.nombre, usuario.primer_ap, usuario.segundo_ap, usuario.fecha_nac))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    #Eliminar usuario
    @classmethod
    def delete_usuario(self, usuario):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM usuario WHERE id = %s", (usuario.id,))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)
        
    # Actualizar usuario 
    @classmethod
    def update_usuario(self, usuario):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE usuario SET ci = %s, nombre = %s, primer_ap = %s, segundo_ap = %s, fecha_nac = %s
                                WHERE id = %s""", (usuario.ci, usuario.nombre, usuario.primer_ap, usuario.segundo_ap, usuario.fecha_nac, usuario.id))
                affected_rows = cursor.rowcount
                connection.commit()
            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)