import psycopg2
from connect import connect

# 1. Search contacts using a FUNCTION (Task 1)
def search_contacts(pattern):
    conn = connect()
    cur = conn.cursor()
    # Functions are called via SELECT
    cur.execute("SELECT * FROM get_contacts_by_pattern(%s)", (pattern,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

# 2. Insert or Update (UPSERT) using a PROCEDURE (Task 2)
def upsert_contact(name, surname, phone):
    conn = connect()
    cur = conn.cursor()
    # Procedures are called via CALL
    cur.execute("CALL upsert_contact(%s, %s, %s)", (name, surname, phone))
    conn.commit()
    print(f"Contact {name} processed.")
    cur.close()
    conn.close()

# 3. Bulk Insert (Multiple contacts) using a PROCEDURE (Task 3)
def bulk_insert(names, surnames, phones):
    conn = connect()
    cur = conn.cursor()
    # Passing arrays to the procedure
    cur.execute("CALL bulk_insert_contacts(%s, %s, %s)", (names, surnames, phones))
    conn.commit()
    print("Bulk insert finished.")
    cur.close()
    conn.close()

# 4. Pagination using a FUNCTION (Task 4)
def get_paginated(limit, offset):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s)", (limit, offset))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

# 5. Delete contact using a PROCEDURE (Task 5)
def delete_contact(search_val):
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL delete_contact(%s)", (search_val,))
    conn.commit()
    print(f"Search for '{search_val}' and deleted if found.")
    cur.close()
    conn.close()

if __name__ == '__main__':
    print("\n--- Practice 8: PhoneBook ---")
    print("1: Search, 2: Upsert, 3: Bulk Insert, 4: Pagination, 5: Delete")
    choice = input("Select action: ")
    
    if choice == '1':
        search_contacts(input("Enter name/phone pattern: "))
    elif choice == '2':
        upsert_contact(input("Name: "), input("Surname: "), input("Phone: "))
    elif choice == '3':
        # Example of bulk insert (test data)
        names = ['Aman', 'Berik']
        surnames = ['Saken', 'Ivanov']
        phones = ['87010001122', '87079998877'] # Must be 11 digits to pass validation
        bulk_insert(names, surnames, phones)
    elif choice == '4':
        get_paginated(int(input("Limit: ")), int(input("Offset: ")))
    elif choice == '5':
        delete_contact(input("Enter name or phone to delete: "))