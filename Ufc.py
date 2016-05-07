import csv
import psycopg2


#conn = psycopg2.connect("dbname=davidvillarreal user=davidvillarreal")
#cur = conn.cursor()
#cur.execute("""DELETE FROM fighters_data""")
#conn.commit()
#cur.close()
#conn.close()



fighter_data = []
with open('fighters.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    #fighter_data = open_csv()
#    header = next(readCSV)
    for row in readCSV:
        fighter_data.append(row[1:])

    print(fighter_data)
    print(type(fighter_data))




conn = psycopg2.connect("dbname=davidvillarreal user=davidvillarreal ")
cur = conn.cursor()

for row in fighter_data:

    cur.execute("""
INSERT INTO fighter_data
            (name,
             nick,
             birth_date,
             height,
             weight)

    VALUES (%s, %s, %s, %s, %s) """, row)

#cur.fetchall()
conn.commit()
cur.close()
conn.close
