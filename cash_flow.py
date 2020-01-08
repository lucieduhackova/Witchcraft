import sqlite3
from sqlite3 import Error

datum =input("Napiš datum ve formátu: RRRR-MM-DD ")
prijem = input("Napiš částku příjmu, pokud žádná, tak 0 ")
vydaj_jidlo = input("Pokud za jídlo napiš částku, pokud ne,napiš 0 ")
vydaj_obleceni = input("Pokud za obleční napiš částku, pokud ne,napiš 0 ")
vydaj_zabava = input("Pokud za zábavu napiš částku, pokud ne,napiš 0 ")
vydaj_fix = input("Pokud za fix napiš částku, pokud ne,napiš 0 ")
# smazat_cely_radek_datum = input("Chceš smazat řádek s datem? Napiš, které datum RRRR-MM-DD ")




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
    Create a new project into the projects table
    :param conn:
    :param project:
    """
    sql = """INSERT INTO cf(date, income, ex_food, ex_clothes, ex_fun, ex_fix) VALUES (?,?,?,?,?,?)"""
    cur = conn.cursor()
    cur.execute(sql, data)
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



def main():
    database = (r"C:\pywitches\Witchcraft\cash_flow.db")

    sql_create_cf_table = """ CREATE TABLE IF NOT EXISTS cf (
                                        date text,
                                        income integer,
                                        ex_food integer,
                                        ex_clothes integer,
                                        ex_fun integer,
                                        ex_fix integer) """


    conn = create_connection(database)


    # create tables
    if conn is not None:
        # create cf table
        create_table(conn, sql_create_cf_table)

    else:
        print("Error! cannot create the database connection.")


    data = (datum, prijem, vydaj_jidlo, vydaj_obleceni, vydaj_zabava, vydaj_fix)
    insert_dates(conn, data)
    # delete_all_row_cf(conn, smazat_cely_radek_datum)

if __name__ == '__main__':
    main()
