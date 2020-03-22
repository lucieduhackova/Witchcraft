import sqlite3
from sqlite3 import Error

rozhodovaci_dotaz = input("Chceš vkládat (v), mazat (m) nebo aktualizovat (a), znat sumu prijmu (s) ")

if rozhodovaci_dotaz == "v":
    datum = input("Napiš datum ve formátu: RRRR-MM-DD ")
    prijem = input("Napiš částku příjmu, pokud žádná, tak 0 ")
    vydaj_jidlo = input("Pokud za jídlo napiš částku, pokud ne,napiš 0 ")
    vydaj_obleceni = input("Pokud za obleční napiš částku, pokud ne,napiš 0 ")
    vydaj_zabava = input("Pokud za zábavu napiš částku, pokud ne,napiš 0 ")
    vydaj_fix = input("Pokud za fix napiš částku, pokud ne,napiš 0 ")
elif rozhodovaci_dotaz == "m":
    datum = input("Napiš datum ve formátu: RRRR-MM-DD ")
elif rozhodovaci_dotaz == "a":
    datum = input("Napiš datum ve formátu: RRRR-MM-DD ")
    prijem = input("Napiš částku příjmu, pokud žádná, tak 0 ")
    vydaj_jidlo = input("Pokud za jídlo napiš částku, pokud ne,napiš 0 ")
    vydaj_obleceni = input("Pokud za obleční napiš částku, pokud ne,napiš 0 ")
    vydaj_zabava = input("Pokud za zábavu napiš částku, pokud ne,napiš 0 ")
    vydaj_fix = input("Pokud za fix napiš částku, pokud ne,napiš 0 ")
elif rozhodovaci_dotaz == "s":
    pass
else:
    print("Nerozumím")
    exit()

# datum =input("Napiš datum ve formátu: RRRR-MM-DD ")
# prijem = input("Napiš částku příjmu, pokud žádná, tak 0 ")
# vydaj_jidlo = input("Pokud za jídlo napiš částku, pokud ne,napiš 0 ")
# vydaj_obleceni = input("Pokud za obleční napiš částku, pokud ne,napiš 0 ")
# vydaj_zabava = input("Pokud za zábavu napiš částku, pokud ne,napiš 0 ")
# vydaj_fix = input("Pokud za fix napiš částku, pokud ne,napiš 0 ")
# smazat_cely_radek_datum = input("chceš smazat řádek s datem? napiš, které datum rrrr-mm-dd ")
# update_radku = input("Chceš přidat data k určitému dni? Napiš datum rrrr-mm-dd")






def create_connection(cash_flow):
    """ create a database connection to the SQLite database
        specified by cash_flow
    :param cash_flow: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(cash_flow)
        return conn
    except Error as e:
        print(e)
    return conn




def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)



def insert_dates(conn, data):
    """
    Create a new project into the cf table
    :param conn:
    :param data:
    """
    sql = """INSERT INTO cf(date, income, ex_food, ex_clothes, ex_fun, ex_fix) VALUES (?,?,?,?,?,?)"""
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()


def update_row(conn, update_radku):
    """
    udělá update dat v řádku, podle data, který zadáme
    :param conn:
    :param update_radku:
    :return: cf data
    """
    sql = ''' UPDATE cf SET income = ?, ex_food = ?, ex_clothes = ?, ex_fun = ?, ex_fix = ? WHERE date = ?'''
    cur = conn.cursor()
    cur.execute(sql, update_radku)
    conn.commit()



def delete_all_row_cf(conn, smazat_cely_radek_datum):
    """
    Smaže celý řádek, kde je obsažené datum, které zadáme
    :param conn:  Connection to the SQLite database
    :param date: date of the expenditure or income
    :return:
    """
    sql = 'DELETE FROM cf WHERE date=?'
    cur = conn.cursor()
    cur.execute(sql, (smazat_cely_radek_datum,))
    conn.commit()

def closing_balance(conn):
    cur = conn.cursor()
    cur.execute("""SELECT SUM("income") - SUM("ex_food") - SUM("ex_clothes") - SUM("ex_fun") - SUM("ex_fix") FROM cf""")
    conn.commit()
    rows = cur.fetchall()
    for row in rows:
        print(row)




def main():
    database = (r"cash_flow.db")

    sql_create_cf_table = """ CREATE TABLE IF NOT EXISTS cf (
                                        date text,
                                        income integer,
                                        ex_food integer,
                                        ex_clothes integer,
                   
                                     ex_fun integer,
                                        ex_fix integer) """


    conn = create_connection(database)


    if conn is not None:
        create_table(conn, sql_create_cf_table)

    else:
        print("Error! cannot create the database connection.")

    if rozhodovaci_dotaz == "v":
        data = (datum, prijem, vydaj_jidlo, vydaj_obleceni, vydaj_zabava, vydaj_fix)
        insert_dates(conn, data)
    elif rozhodovaci_dotaz == "m":
        delete_all_row_cf(conn, datum)
    elif rozhodovaci_dotaz == "a":
        update_radku = (prijem, vydaj_jidlo, vydaj_obleceni, vydaj_zabava, vydaj_fix, datum)
        update_row(conn, update_radku)
    elif rozhodovaci_dotaz == "s":
        closing_balance(conn)




if __name__ == '__main__':
    main()


