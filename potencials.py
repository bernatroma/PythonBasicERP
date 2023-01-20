from tkinter import * 
from tkinter import ttk 
import sqlite3
import tkinter as tk
from tkinter import PhotoImage
from emails import potencials_mail,sendmail
from analiticas import potanalitica

nominput = None
email_entry = None
phone_entry = None
address_entry = None


def submit():
    name = nominput.get()
    email = email_entry.get()
    phone = phone_entry.get()
    address = address_entry.get()
    con = sqlite3.connect("db/elfos.db")
    cur = con.cursor()
    cur.execute("INSERT INTO clientes_pot (name, email, phone, address) VALUES (?, ?, ?, ?)", (name, email, phone, address))
    con.commit()
    print("Registre afegit ",name, email, phone, address)
    con.close()



def addclients():
    global nominput
    global email_entry
    global phone_entry
    global address_entry
    addventana = tk.Tk()
    addventana.title('Afegeix Clients Potencials')
    addventana.geometry('400x400')
    nom = tk.Label(addventana, text="Nom:")
    nom.pack()
    nominput = tk.Entry(addventana)
    nominput.pack()
    email_label = tk.Label(addventana, text="Email:")
    email_label.pack()
    email_entry = tk.Entry(addventana)
    email_entry.pack()
    phone_label = tk.Label(addventana, text="Telefon:")
    phone_label.pack()
    phone_entry = tk.Entry(addventana)
    phone_entry.pack()
    address_label = tk.Label(addventana, text="Adreça:")
    address_label.pack()
    address_entry = tk.Entry(addventana)
    address_entry.pack()
    submit_button = tk.Button(addventana, text="Submit", command=submit)
    submit_button.pack()

    addventana.mainloop()

    
def seeclients():
    veureClients = tk.Tk()
    veureClients.geometry('200x200')
    veureClients.configure(bg = 'beige')
    veureClients.title('Clients')
    text=Text(veureClients, width=80, height=15)
    text.pack()
    con = sqlite3.connect("db/elfos.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM clientes_pot")
    resultado = cur.fetchall()
    for row in resultado:
        name = row[0]
        email = row[1]
        phone = row[2]
        address = row[3]
        text.insert('1.0', f'Nom: {name}\nEmail: {email}\nTelefon: {phone}\nAdreca: {address}\n\n')
    con.commit()
    con.close()
    veureClients.mainloop()



def modifyclients():
    update_ventana = tk.Tk()
    update_ventana.title("Modificar Client Potencial")
    update_ventana.geometry("400x400")

    nom = tk.Label(update_ventana, text="Nom Client a modificar:")
    nom.pack()
    nominput = tk.Entry(update_ventana)
    nominput.pack()

    nounom = tk.Label(update_ventana, text="Nou Nom:")
    nounom.pack()
    nounominput = tk.Entry(update_ventana)
    nounominput.pack()

    new_email_label = tk.Label(update_ventana, text="Nou Email:")
    new_email_label.pack()
    new_email_entry = tk.Entry(update_ventana)
    new_email_entry.pack()

    numerotel = tk.Label(update_ventana, text="Nou Numero de Telèfon:")
    numerotel.pack()
    numerotel_input = tk.Entry(update_ventana)
    numerotel_input.pack()

    adreca = tk.Label(update_ventana, text="Nova Adreça:")
    adreca.pack()
    adreca_input = tk.Entry(update_ventana)
    adreca_input.pack()

    submit = tk.Button(update_ventana, text="Submit", command=lambda: modificar_sub(nominput.get(), nounominput.get(), new_email_entry.get(), numerotel_input.get(), adreca_input.get()))
    submit.pack()
    update_ventana.mainloop()

def modificar_sub(name, new_name, new_email, new_phone, new_address):
    con = sqlite3.connect("db/elfos.db")
    cur = con.cursor()
    cur.execute("UPDATE clientes_pot SET name = ?, email = ?, phone = ?, address = ? WHERE name = ?", (new_name, new_email, new_phone, new_address, name))
    con.commit()
    con.close()


def eliminarclients():
    delete_ventana = tk.Tk()
    delete_ventana.title("Eliminar Client Potencials")
    delete_ventana.geometry("400x400")

    con = sqlite3.connect("db/elfos.db")
    cur = con.cursor()
    cur.execute("SELECT name FROM clientes_pot")
    result = cur.fetchall()
    client_list = [client[0] for client in result]

    for client in client_list:
        ttk.Button(delete_ventana, text=client, command=lambda: eliminar(client)).pack()
    
    delete_ventana.mainloop()

def eliminar(client):
    con = sqlite3.connect("db/elfos.db")
    cur = con.cursor()
    cur.execute("DELETE FROM clientes_pot WHERE name=?", (client,))
    con.commit()
    con.close()

def submitmail():
    global remitenteInput
    global mensajeInput
    global asuntoInput
    global passwordInput
    remitente = remitenteInput.get()
    mensaje = mensajeInput.get()
    asunto = asuntoInput.get()
    password = passwordInput.get()
    emails = potencials_mail()
    for mails in emails:
        sendmail(remitente, mails, mensaje, asunto, password)


def mail():
    global remitenteInput
    global mensajeInput
    global asuntoInput
    global passwordInput

    mail_ventana = tk.Tk()
    mail_ventana.title("Enviar Mail Clients")
    mail_ventana.geometry("400x400")

    remitente = tk.Label(mail_ventana, text="Email del Remitent:")
    remitente.pack()
    remitenteInput = tk.Entry(mail_ventana)
    remitenteInput.pack()


    mensaje = tk.Label(mail_ventana, text="Cos del Missatge:")
    mensaje.pack()
    mensajeInput = tk.Entry(mail_ventana)
    mensajeInput.pack()

    asunto = tk.Label(mail_ventana, text="Asunto del Missatge:")
    asunto.pack()
    asuntoInput = tk.Entry(mail_ventana)
    asuntoInput.pack()

    password = tk.Label(mail_ventana, text="Contrasenya Remitent:")
    password.pack()
    passwordInput = tk.Entry(mail_ventana)
    passwordInput.pack()

    submit_button = tk.Button(mail_ventana, text="Submit", command=submitmail)
    submit_button.pack()




def clients_pot():
    ventanaClients = Tk()
    ventanaClients.geometry('1600x1000')
    ventanaClients.configure(bg = 'beige')
    ventanaClients.title('Clients Potencials')
    label = Label(ventanaClients, text="Menu de Clients Potencials")
    label.config(font=('Helvetica bold', 16))
    label.pack()    

    
    afegirboton = ttk.Button(ventanaClients, text='Afegir Clients Potencials', command=addclients)
    afegirboton.place(width=180,height=100,relx=0.25, rely=0.35, anchor=W)
    veureboton = ttk.Button(ventanaClients, text='Veure Clients Potencials', command=seeclients)
    veureboton.place(width=180,height=100,relx=0.45, rely=0.35, anchor=W)
    modifyboton = ttk.Button(ventanaClients, text='Modificar Clients Potencials', command=modifyclients)
    modifyboton.place(width=180,height=100,relx=0.65, rely=0.35, anchor=W)
    elimarboton = ttk.Button(ventanaClients, text='Eliminar Clients Potencials', command=eliminarclients)
    elimarboton.place(width=180,height=100,relx=0.25, rely=0.6, anchor=W)
    enviarmailboton = ttk.Button(ventanaClients, text='Mail Clients Potencials', command=mail)
    enviarmailboton.place(width=180,height=100,relx=0.45, rely=0.6, anchor=W)
    analitapot = ttk.Button(ventanaClients, text='Analitica Nom Clients', command=potanalitica)
    analitapot.place(width=180,height=100,relx=0.65, rely=0.6, anchor=W)
    
    sortirboton = ttk.Button(ventanaClients, text='Sortir', command=quit)
    sortirboton.place(width=180,height=100,relx=0.45, rely=0.78, anchor=W)

