import tkinter as tk
from tkinter import messagebox, Listbox

import mysql.connector

def create_database():
    db_name = db_entry.get()
    if db_name == "":
        messagebox.showinfo("Create Database", "Please enter a database name.")
        return

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Taki imrane66"
    )
    mycursor = mydb.cursor()
    mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
    mydb.close()

    messagebox.showinfo("Create Database", f"Database '{db_name}' created successfully.")

def create_table():
    db_name = db_entry.get()
    table_name = table_entry.get()
    if db_name == "" or table_name == "":
        messagebox.showinfo("Create Table", "Please enter both database and table name.")
        return

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Taki imrane66",
        database=db_name
    )
    mycursor = mydb.cursor()
    mycursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id INT AUTO_INCREMENT PRIMARY KEY, firstname VARCHAR(255), lastname VARCHAR(255),date_naissance DATE, age INT, taille DECIMAL(10,2),poids DECIMAL(10,2), nationalite VARCHAR(255), position VARCHAR(255), shirt_number INT, strong_foot VARCHAR(255), salaire VARCHAR(255) ,debut_contrat DATE ,fin_contrat DATE)")
    mydb.close()

    messagebox.showinfo("Create Table", f"Table '{table_name}' created successfully.")

def insert():
    db_name = db_entry.get()
    id_val = e_id.get()
    firstname_val = e_firstname.get()
    lastname_val = e_lastname.get()
    date_naissance_val = e_date_naissance.get()
    age_val = e_age.get()
    taille_val = e_t.get()
    poids_val = e_p.get()
    nationalite_val = e_nat.get()
    position_val = e_poste.get()
    shirt_val = e_num.get()
    strong_foot_val = e_strong_foot.get()
    salaire_val = e_salaire.get()
    debut_val = e_date_d.get()
    fin_val = e_date_f.get()


    if db_name == "" or id_val == "" or firstname_val == "" or lastname_val == "" or date_naissance_val == "" or age_val=="" or taille_val == "" or poids_val == "" or nationalite_val == "" or position_val == "" or shirt_val == "" or strong_foot_val == "" or salaire_val == "" or debut_val == "" or fin_val == "" :
        messagebox.showinfo("Insert Status", "All fields are required.")
        return

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Taki imrane66",
        database=db_name
    )
    mycursor = mydb.cursor()
    mycursor.execute(f"INSERT INTO {table_entry.get()} (id , firstname, lastname ,date_naissance , age , taille ,poids, nationalite, position , shirt_number , strong_foot , salaire  ,debut_contrat  ,fin_contrat ) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s,%s,%s,%s)", (id_val, firstname_val, lastname_val,date_naissance_val,age_val,taille_val,poids_val,nationalite_val,position_val,shirt_val,strong_foot_val,salaire_val,debut_val,fin_val))
    mydb.commit()
    mydb.close()
    e_id.delete(0,"end")
    e_firstname.delete(0,"end")
    e_lastname.delete(0,"end")
    e_date_naissance.delete(0,"end")
    e_age.delete(0,"end")
    e_t.delete(0,"end")
    e_p.delete(0,"end")
    e_nat.delete(0,"end")
    e_poste.delete(0,"end")
    e_num.delete(0,"end")
    e_strong_foot.delete(0,"end")
    e_salaire.delete(0,"end")
    e_date_d.delete(0,"end")
    e_date_f.delete(0,"end")
    show()
    messagebox.showinfo("Insert Status", "Record inserted successfully.")
    mydb.close()

def delete():
    db_name = db_entry.get()
    id_val = e_id.get()

    if db_name == "" or id_val == "":
        messagebox.showinfo("Delete Status", "Database name and ID are required.")
        return

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Taki imrane66",
        database=db_name
    )
    mycursor = mydb.cursor()
    mycursor.execute(f"DELETE FROM {table_entry.get()} WHERE id = %s", (id_val,))
    mydb.commit()
    mydb.close()
    e_id.delete(0,"end")
    e_firstname.delete(0,"end")
    e_lastname.delete(0,"end")
    e_age.delete(0,"end")
    e_date_naissance.delete(0,"end")
    e_t.delete(0,"end")
    e_p.delete(0,"end")
    e_nat.delete(0,"end")
    e_poste.delete(0,"end")
    e_num.delete(0,"end")
    e_strong_foot.delete(0,"end")
    e_salaire.delete(0,"end")
    e_date_d.delete(0,"end")
    e_date_f.delete(0,"end")
    show()
    messagebox.showinfo("Delete Status", "Record deleted successfully.")
    mydb.close()

def update():
    db_name = db_entry.get()
    id_val = e_id.get()
    firstname_val = e_firstname.get()
    lastname_val = e_lastname.get()
    date_naissance_val = e_date_naissance.get()
    age_val = e_age.get()
    taille_val = e_t.get()
    poids_val = e_p.get()
    nationalite_val = e_nat.get()
    position_val = e_poste.get()
    shirt_val = e_num.get()
    strong_foot_val = e_strong_foot.get()
    salaire_val = e_salaire.get()
    debut_val = e_date_d.get()
    fin_val = e_date_f.get()

    if db_name == "" or id_val == "" or firstname_val == "" or lastname_val == "" or date_naissance_val == "" or age_val=="" or taille_val == "" or poids_val == "" or nationalite_val == "" or position_val == "" or shirt_val == "" or strong_foot_val == "" or salaire_val == "" or debut_val == "" or fin_val == "":
        messagebox.showinfo("Update Status", "All fields are required.")
        return

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Taki imrane66",
        database=db_name
    )
    mycursor = mydb.cursor()
    # mycursor.execute(f"UPDATE {table_entry.get()} SET firstname = %s, lastname = %s WHERE id = %s", (firstname_val, lastname_val, id_val,date_naissance_val,age_val,taille_val,poids_val,nationalite_val,position_val,shirt_val,strong_foot_val,salaire_val,debut_val,fin_val))
    mycursor.execute(f"UPDATE {table_entry.get()} SET firstname = %s, lastname = %s WHERE id = %s", (firstname_val, lastname_val, id_val))
    mydb.commit()
    mydb.close()
    e_id.delete(0,"end")
    e_firstname.delete(0,"end")
    e_lastname.delete(0,"end")
    e_age.delete(0,"end")
    e_date_naissance.delete(0,"end")
    e_t.delete(0,"end")
    e_p.delete(0,"end")
    e_nat.delete(0,"end")
    e_poste.delete(0,"end")
    e_num.delete(0,"end")
    e_strong_foot.delete(0,"end")
    e_salaire.delete(0,"end")
    e_date_d.delete(0,"end")
    e_date_f.delete(0,"end")
    show()
    messagebox.showinfo("Update Status", "Record updated successfully.")
    mydb.close()

def get():
    db_name = db_entry.get()
    id_val = e_id.get()

    if db_name == "" or id_val == "":
        messagebox.showinfo("Fetch Status", "Database name and ID are required.")
        return

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Taki imrane66",
        database=db_name
    )
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT * FROM {table_entry.get()} WHERE id = %s", (id_val,))
    records = mycursor.fetchall()

    if records:
        for record in records:
            e_firstname.delete(0, "end")
            e_lastname.delete(0, "end")
            e_date_naissance.delete(0,"end")
            e_t.delete(0,"end")
            e_p.delete(0,"end")
            e_nat.delete(0,"end")
            e_poste.delete(0,"end")
            e_num.delete(0,"end")
            e_strong_foot.delete(0,"end")
            e_salaire.delete(0,"end")
            e_date_d.delete(0,"end")
            e_date_f.delete(0,"end")
            e_firstname.insert(0, record[1])
            e_lastname.insert(0, record[2])
            e_date_naissance.insert(0,record[3])
            e_age.insert(0,record[4])
            e_t.insert(0,record[5])
            e_p.insert(0,record[6])
            e_nat.insert(0,record[7])
            e_poste.insert(0,record[8])
            e_num.insert(0,record[9])
            e_strong_foot.insert(0,record[10])
            e_salaire.insert(0,record[11])
            e_date_d.insert(0,record[12])
            e_date_f.insert(0,record[13])
    else:
        messagebox.showinfo("Fetch Status", "No record found.")

    mydb.close()

def show():
    db_name = db_entry.get()

    if db_name == "":
        messagebox.showinfo("Show Status", "Please enter a database name.")
        return

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Taki imrane66",
        database=db_name
    )
    mycursor = mydb.cursor()
    mycursor.execute(f"SELECT * FROM {table_entry.get()}")
    records = mycursor.fetchall()

    listbox.delete(0, "end")

    if records:
        for record in records:
            listbox.insert("end", f"{record[0]} | {record[1]} | {record[2]} | age : {record[4]}")
    else:
        messagebox.showinfo("Show Status", "No records found.")

    mydb.close()

root = tk.Tk()
root.geometry("800x600")
root.title("Mini-projet")

# Database and table creation widgets
db_label = tk.Label(root, text="Enter Database Name:", font=('bold', 10))
db_label.place(x=20, y=30)

db_entry = tk.Entry(root, font=('Arial', 10))
db_entry.place(x=200, y=30)

create_db_button = tk.Button(root, text="Create Database", font=("Arial", 10), bg="blue", command=create_database)
create_db_button.place(x=350, y=30)

table_label = tk.Label(root, text="Enter Table Name:", font=('bold', 10))
table_label.place(x=20, y=60)

table_entry = tk.Entry(root, font=('Arial', 10))
table_entry.place(x=200, y=60)

create_table_button = tk.Button(root, text="Create Table", font=("Arial", 10), bg="blue", command=create_table)
create_table_button.place(x=350, y=60)

# Entry fields for data manipulation
id_label = tk.Label(root, text="Enter ID:", font=('bold', 10))
id_label.place(x=20, y=100)

e_id = tk.Entry(root, font=('Arial', 10))
e_id.place(x=100, y=100)

firstname_label = tk.Label(root, text="Enter your first name:", font=("bold", 10))
firstname_label.place(x=20, y=130)

e_firstname = tk.Entry(root, font=('Arial', 10))
e_firstname.place(x=175, y=130)

lastname_label = tk.Label(root, text="Enter your last name:", font=("bold", 10))
lastname_label.place(x=20, y=160)

e_lastname = tk.Entry(root, font=('Arial', 10))
e_lastname.place(x=175, y=160)

date_naissance_label = tk.Label(root, text="Enter your date de naissance:", font=("bold", 10))
date_naissance_label.place(x=20, y=190)

e_date_naissance = tk.Entry(root, font=('Arial', 10))
e_date_naissance.place(x=200, y=190)

age_label = tk.Label(root, text="Enter your age:", font=("bold", 10))
age_label.place(x=20, y=220)

e_age = tk.Entry(root, font=('Arial', 10))
e_age.place(x=175, y=220)

t_label = tk.Label(root, text="Enter your taille:", font=("bold", 10))
t_label.place(x=20, y=250)

e_t = tk.Entry(root, font=('Arial', 10))
e_t.place(x=175, y=250)

p_label = tk.Label(root, text="Enter your poids:", font=("bold", 10))
p_label.place(x=20, y=280)

e_p = tk.Entry(root, font=('Arial', 10))
e_p.place(x=175, y=280)

num_label = tk.Label(root, text="Enter your shirt number:", font=("bold", 10))
num_label.place(x=20, y=370)

e_num = tk.Entry(root, font=('Arial', 10))
e_num.place(x=175, y=370)


strong_foot_label = tk.Label(root, text="Enter your strong foot :", font=("bold", 10))
strong_foot_label.place(x=20, y=400)

e_strong_foot = tk.Entry(root, font=('Arial', 10))
e_strong_foot.place(x=175, y=400)

salaire_label = tk.Label(root, text="Enter your salary:", font=("bold", 10))
salaire_label.place(x=20, y=430)

e_salaire = tk.Entry(root, font=('Arial', 10))
e_salaire.place(x=175, y=430)

poste_label = tk.Label(root, text="Enter your position:", font=("bold", 10))
poste_label.place(x=20, y=340)

e_poste = tk.Entry(root, font=('Arial', 10))
e_poste.place(x=175, y=340)

nat_label = tk.Label(root, text="Enter your nationality:", font=("bold", 10))
nat_label.place(x=20, y=310)

e_nat = tk.Entry(root, font=('Arial', 10))
e_nat.place(x=175, y=310)


date_d_label = tk.Label(root, text="Enter your date de début de contrat : ", font=("bold", 10))
date_d_label.place(x=20, y=460)

e_date_d = tk.Entry(root, font=('Arial', 10))
e_date_d.place(x=250, y=460)

date_f_label = tk.Label(root, text="Enter your date de fin de contrat :", font=("bold", 10))
date_f_label.place(x=20, y=490)

e_date_f = tk.Entry(root, font=('Arial', 10))
e_date_f.place(x=250, y=490)

# Buttons for data manipulation
insert_button = tk.Button(root, text="Ajouter", font=("Arial", 10), bg="blue", command=insert)
insert_button.place(x=20, y=520)

delete_button = tk.Button(root, text="Supprimer", font=("Arial", 10), bg="blue", command=delete)
delete_button.place(x=80, y=520)

update_button = tk.Button(root, text="Modifier", font=("Arial", 10), bg="blue", command=update)
update_button.place(x=157, y=520)

get_button = tk.Button(root, text="afficher", font=("Arial", 10), bg="blue", command=get)
get_button.place(x=250, y=520)


listbox = Listbox(root, width=50,height=25) 
listbox.place(x=690, y=30)

show_button = tk.Button(root, text="Afficher tous", font=("Arial", 10), bg="blue", command=show)
show_button.place(x=550, y=220)


root.mainloop()
