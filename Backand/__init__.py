def conectardb():
    con = psycopg2.connect(

        host='localhost',
        database='Banco/backand',
        user='postgres',
        password='937251'
    )
    return con

conectardb()

