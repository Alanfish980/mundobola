import psycopg2

def conectardb():

    con = psycopg2.connect(

        host='localhost',
        database = 'cachorrro',
        user = 'postgres',
        password = '937251'
    )
    return con


def login(user, senha):
    con = conectardb()
    cur = con.cursor()
    sq = f"SELECT * from usuario where login='{user}' and senha='{senha}'"
    cur.execute(sq)
    saida = cur.fetchall()

    cur.close()
    con.close()

    return saida


def inserir_user(nome, login, senha):

    conn = conectardb()
    cur = conn.cursor()
    try:
        sql = f"INSERT INTO usuario (nome, login, senha) VALUES ('{nome}','{login}','{senha}')"
        cur.execute(sql)

    except psycopg2.IntegrityError:
        conn.rollback()
        exito = False
    else:
        conn.commit()
        exito = True

    cur.close()
    conn.close()
    return exito

def listar_usuarios():
    con = conectardb()
    cur = con.cursor()
    sq = f"SELECT  nome, login from usuario"
    cur.execute(sq)
    saida = cur.fetchall()

    cur.close()
    con.close()

    return saida