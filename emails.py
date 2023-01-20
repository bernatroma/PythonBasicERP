from email.message import EmailMessage
import smtplib
import sqlite3


def clients_mail():
    conn = sqlite3.connect('db/elfos.db')
    cursor = conn.cursor()
    cursor.execute("SELECT email FROM clientes")
    emails = cursor.fetchall()
    conn.close()
    email_list = [email[0] for email in emails]
    return email_list


def proveidors_mail():
    conn = sqlite3.connect('db/elfos.db')
    cursor = conn.cursor()
    cursor.execute("SELECT mail FROM proveidors")
    emails = cursor.fetchall()
    conn.close()
    email_list = [email[0] for email in emails]
    return email_list


def  potencials_mail():
    conn = sqlite3.connect('db/elfos.db')
    cursor = conn.cursor()
    cursor.execute("SELECT email FROM clientes_pot")
    emails = cursor.fetchall()
    conn.close()
    email_list = [email[0] for email in emails]
    return email_list


def sendmail(remitente,destinatario,mensaje,asunto,password):
    # PER ENVIAR MAILS AMB EL SERVER DE GMAIL NECESITES CREAR UNA CONTRASENYA ESPECIAL 
    # https://www.letscodemore.com/blog/smtplsmtplibib-smtpauthenticationerror-username-and-password-not-accepted/

    remitente = remitente
    destinatario = destinatario
    mensaje = mensaje
    email = EmailMessage()
    email["From"] = remitente
    email["To"] = destinatario
    email["Subject"] = asunto
    email.set_content(mensaje)
    smtp = smtplib.SMTP_SSL("smtp.gmail.com")
    smtp.login(remitente, password)
    smtp.sendmail(remitente, destinatario, email.as_string())
    smtp.quit()

