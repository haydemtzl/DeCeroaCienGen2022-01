from sqlalchemy import create_engine
import pymysql
import pandas as pd

#string de conexión se necesita tener el user de la bd, contraseña, host y nombre de la bd
db_connection = 'mysql+pymysql://mysql_user:mysql_password@mysql_host/mysql_db'
conn = create_engine(db_connection)

df = pd.read_sql("select * from tab_name", conn)
