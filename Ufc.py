import csv
import psycopg2

def delete_data():
    conn = psycopg2.connect("dbname=davidvillarreal user=davidvillarreal")
    cur = conn.cursor()
    cur.execute("""DELETE FROM fighters_data""")
    conn.commit()
    cur.close()
    conn.close()

def open_csv():
    with open('fighters.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        header = next(readCSV)
        names = []
        nicks = []
        birth_dates = []
        heights = []
        weights = []
        associations = []
        classes = []
        localities = []
        countries = []
        for row in readCSV:


            names.append(row[2])
            nicks.append(row[3])
            birth_dates.append(row[4])
            heights.append(row[5])
            weights.append(row[6])
            associations.append(row[7])
            classes.append(row[8])
            localities.append(row[9])
            countries.append(row[10])

        print(names)
        print(nicks)
        print(birth_dates)
        print(heights)
        print(weights)
        print(associations)
        print(classes)
        print(localities)
        print(countries)



def insert_data(aList):
    conn = psycopg2.connect("dbname=davidvillarreal user='davidvillarreal ")
    cur = conn.cursor()
    for row in aList:

        cur.execute("""
    INSERT INTO  fighter_data
                (name,
                 nick,
                 birth_date,
                 height,
                 weight,
                 association,
                 class,
                 locality,
                 country)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)""", row)

    cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
