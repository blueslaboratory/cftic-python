# Day 14 - 16/06/2023
# Ejercicios Mix

import mysql.connector
from mysql.connector.errors import DatabaseError

def crear_tabla(n_tabla):
    try:
        bbdd = mysql.connector.connect(host='localhost',
                                       port='3306',
                                       database='hr',
                                       user='HR',
                                       password='hr')
        cursor = bbdd.cursor()
        sql = f"""
              SELECT COUNT(*) FROM information_schema.tables 
        WHERE table_schema = 'HR' AND table_name = '{n_tabla}'
              """
        cursor.execute(sql)
        valor=cursor.fetchone()

        if not valor[0]:
            sql=f"""
               CREATE  TABLE IF NOT EXISTS `{n_tabla}` (
              `id` INT NOT NULL AUTO_INCREMENT,
              `nombre` VARCHAR(45) NOT NULL,
              `edad` INT(2) NULL,
              `genero` INT(1) NULL,
              `ocupacion` VARCHAR(45) NULL,
              PRIMARY KEY (`id`))"""
            cursor.reset() ##### Es conveniente resetearlo para que ocurran errores indeterminado
            cursor.execute(sql)

        cursor.close()
    except DatabaseError:
     print('Se ha producido un error de base de datos')
    finally:
     bbdd.close()



def insertar_datos(datos):
    try:
        bbdd = mysql.connector.connect(host='localhost',
                                       port='3306',
                                       database='hr',
                                       user='HR',
                                       password='hr')
        cursor = bbdd.cursor()
        sql ='''
            INSERT INTO persona (nombre,edad,genero,ocupacion)
            VALUES (%s,%s,%s,%s)
            '''
        for dato in datos:
            cursor.execute(sql,dato)
            print('Se han insertado',cursor.rowcount,'registros')
            cursor.reset()
        bbdd.commit()
        cursor.close()
    except DatabaseError:
     print('Se ha producido un error de base de datos')
    finally:
        bbdd.close()


crear_tabla('fichero')

datos=[('Juan Pérez',30,0,'Ingeniero'), ('María García',25,1,'Doctora')]
insertar_datos(datos)