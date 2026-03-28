import psycopg2
import csv
from connect import connect

# 1. Manual Insert (Task 3.2.3)
def insert_contact(first_name, last_name, phone_number):
    sql = "INSERT INTO contacts(first_name, last_name, phone_number) VALUES(%s, %s, %s);"
    conn = None
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, (first_name, last_name, phone_number))
        conn.commit()
        print(f"Contact {first_name} inserted!")
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn: conn.close()

# 2. CSV Import (Task 3.2.2)
def insert_from_csv(file_path):
    sql = "INSERT INTO contacts(first_name, last_name, phone_number) VALUES(%s, %s, %s);"
    conn = None
    try:
        conn = connect()
        cur = conn.cursor()
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                cur.execute(sql, (row[0], row[1], row[2]))
        conn.commit()
        print("CSV data imported!")
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn: conn.close()

# 3. Update Contact (Task 3.2.4)
def update_contact_phone(first_name, new_phone):
    sql = "UPDATE contacts SET phone_number = %s WHERE first_name = %s;"
    conn = None
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, (new_phone, first_name))
        conn.commit()
        print(f"Contact {first_name} updated!")
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn: conn.close()

# 4. Querying/Filtering (Task 3.2.5)
def get_contacts_by_name(name_pattern):
    sql = "SELECT * FROM contacts WHERE first_name LIKE %s;"
    conn = None
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, (name_pattern + '%',)) # Find names starting with pattern
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn: conn.close()

# 5. Delete Contact (Task 3.2.6)
def delete_contact(first_name):
    sql = "DELETE FROM contacts WHERE first_name = %s;"
    conn = None
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, (first_name,))
        conn.commit()
        print(f"Contact {first_name} deleted!")
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn: conn.close()

if __name__ == '__main__':
    # Меню для проверки всех функций
    print("\n1: Insert, 2: CSV, 3: Update, 4: Search, 5: Delete")
    choice = input("Select action: ")
    
    if choice == '1':
        insert_contact(input("Name: "), input("Last name: "), input("Phone: "))
    elif choice == '2':
        insert_from_csv('contacts.csv')
    elif choice == '3':
        update_contact_phone(input("Name to update: "), input("New phone: "))
    elif choice == '4':
        get_contacts_by_name(input("Search name: "))
    elif choice == '5':
        delete_contact(input("Name to delete: "))