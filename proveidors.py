from tkinter import *
from tkinter import ttk
import sqlite3
from analiticas import analitaproveidors
import tkinter as tk
from tkinter import PhotoImage
from emails import proveidors_mail,sendmail


def submit():
    nom = nominput.get()
    email = email_entry.get()
    telefon = phone_entry.get()
    adreca = address_entry.get()
    con = sqlite3.connect("db/elfos.db")
    cur = con.cursor()
    cur.execute("INSERT INTO proveidors (nom, direccio, mail, telefon) VALUES (?, ?, ?, ?)", (nom, adreca, email, telefon))
    con.commit()
    con.close()

def addproveidors():
    global nominput
    global email_entry
    global phone_entry
    global address_entry
    addventana = tk.Tk()
    addventana.title('Afegeix proveidors')
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


def seeproveidors():
    veureClients = tk.Tk()
    veureClients.geometry('200x200')
    veureClients.configure(bg = 'beige')
    veureClients.title('Proveidors')
    text=Text(veureClients, width=80, height=15)
    text.pack()
    con = sqlite3.connect("db/elfos.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM proveidors")
    resultado = cur.fetchall()
    for row in resultado:
        nom = row[0]
        adreca = row[1]
        email = row[2]
        telefon = row[3]
        text.insert('1.0', f'Name: {nom}\nAdreca: {adreca}\nEmail: {email}\nTelefon: {telefon}\n\n')
    con.commit()
    con.close()
    veureClients.mainloop()

def modifyclients():
    update_ventana = tk.Tk()
    update_ventana.title("Modificar Proveidor")
    update_ventana.geometry("400x400")

    nom = tk.Label(update_ventana, text="Nom Proveidor a modificar:")
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
    cur.execute("UPDATE proveidors SET nom = ?, mail = ?, telefon = ?, direccio = ? WHERE nom = ?", (new_name, new_email, new_phone, new_address, name))
    con.commit()
    con.close()

def eliminarproveidors():
    delete_ventana = tk.Tk()
    delete_ventana.title("Eliminar Proveidor")
    delete_ventana.geometry("400x400")

    con = sqlite3.connect("db/elfos.db")
    cur = con.cursor()
    cur.execute("SELECT nom FROM proveidors")
    result = cur.fetchall()
    proveidor_list = [proveidor[0] for proveidor in result]

    for proveidor in proveidor_list:
        ttk.Button(delete_ventana, text=proveidor, command=lambda: eliminar(proveidor)).pack()
    
    delete_ventana.mainloop()

def eliminar(proveidor):
    con = sqlite3.connect("db/elfos.db")
    cur = con.cursor()
    cur.execute("DELETE FROM proveidors WHERE nom=?", (proveidor,))
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
    emails = proveidors_mail()
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


def proveidors():
    ventanaProveidors = Tk()
    ventanaProveidors.geometry('1600x1000')
    ventanaProveidors.configure(bg = 'beige')
    ventanaProveidors.title('Proveidors')
    label = Label(ventanaProveidors, text="Menu de Proveidors")
    label.config(font=('Helvetica bold', 16))
    label.pack()    

    afegirboton = ttk.Button(ventanaProveidors, text='Afegir Proveidors', command=addproveidors)
    afegirboton.place(width=180,height=100,relx=0.25, rely=0.35, anchor=W)
    veureboton = ttk.Button(ventanaProveidors, text='Veure Proveidors', command=seeproveidors)
    veureboton.place(width=180,height=100,relx=0.45, rely=0.35, anchor=W)

    modifyprov = ttk.Button(ventanaProveidors, text='Modificar Proveidors', command=modifyclients)
    modifyprov.place(width=180,height=100,relx=0.65, rely=0.35, anchor=W)

    eliminarboton = ttk.Button(ventanaProveidors, text='Eliminar Proveidors', command=eliminarproveidors)
    eliminarboton.place(width=180,height=100,relx=0.25, rely=0.6, anchor=W)

    enviarboton = ttk.Button(ventanaProveidors, text='Enviar Mail Proveidors', command=mail)
    enviarboton.place(width=180,height=100,relx=0.45, rely=0.6, anchor=W)
    
    analtcaboto = ttk.Button(ventanaProveidors, text='Crear Gràfic Nom', command=analitaproveidors)
    analtcaboto.place(width=180,height=100,relx=0.65, rely=0.6, anchor=W)

    sortirboton = ttk.Button(ventanaProveidors, text='Sortir', command=quit)
    sortirboton.place(width=180,height=100,relx=0.45, rely=0.78, anchor=W)