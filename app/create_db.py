import psycopg2

conn = psycopg2.connect(
   database="POSTGRES",
   user="POSTGRES",
   password="POSTGRES",
   host="db",
   port="5432",
)


cur = conn.cursor()

cur.execute('''
    CREATE TABLE pessoa (
            id uuid DEFAULT gen_random_uuid(),
            nome TEXT,
            apelido TEXT,
            nascimento TEXT,
            stack text[],
            PRIMARY KEY (id)
    );
''')

conn.commit()

conn.close()