from DBConnection import get_connection

def add_beneficiary(name, card_no, family_size, category):
    con = get_connection()
    cursor = con.cursor()
    query = "INSERT INTO beneficiary (name, card_no, family_size, category) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (name, card_no, family_size, category))
    con.commit()
    print("✅ Beneficiary added successfully!")
    con.close()

def view_beneficiaries():
    con = get_connection()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM beneficiary")
    for row in cursor.fetchall():
        print(row)
    con.close()

def update_beneficiary(id, name, family_size, category):
    con = get_connection()
    cursor = con.cursor()
    query = "UPDATE beneficiary SET name=%s, family_size=%s, category=%s WHERE id=%s"
    cursor.execute(query, (name, family_size, category, id))
    con.commit()
    print("✅ Beneficiary updated successfully!")
    con.close()

def delete_beneficiary(id):
    con = get_connection()
    cursor = con.cursor()
    query = "DELETE FROM beneficiary WHERE id=%s"
    cursor.execute(query, (id,))
    con.commit()
    print("🗑️ Beneficiary deleted!")
    con.close()
