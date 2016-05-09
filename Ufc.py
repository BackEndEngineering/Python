import csv
import psycopg2
fighter_data = []


def delete_data():
    conn = psycopg2.connect("dbname=davidvillarreal user=davidvillarreal")
    cur = conn.cursor()
    delete_file = input("what file do you want to delete? ")
    cur.execute('DELETE FROM %s' % delete_file)
    conn.commit()
    cur.close()
    conn.close()
    port = input(" Type Import Data to Import or No to finished \n")
    port = port.lower()
    if port == "import data":
        answer = import_data()
    elif install == 'no':
        print('program terminated')


def import_data():
    with open('fighters.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            fighter_data.append(row[2:7])
        print(fighter_data)
        install = input("Type Install Data to Install or NO to finished \n")
        install = install.lower()
        if install == "install data":
            answer = install_data()
        elif install == 'no':
            print('program terminated')


def install_data():
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
    conn.commit()
    cur.close()
    conn.close


def data():
    data = input(" Type Import Data or Delete Data \n")
    data = data.lower()
    if data == 'import data':
        answer = import_data()
    elif data == 'delete data':
        answer = delete_data()
    return answer


def main():
    answer = data()


if __name__ == '__main__':
    main()
