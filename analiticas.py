import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

def analitaclientes():
    conn = sqlite3.connect("db/elfos.db")
    clientes = pd.read_sql_query("SELECT * from clientes", conn)
    nombres = clientes["name"].value_counts()
    nombres.plot(kind="bar")
    plt.show()

def analitaproveidors():
    conn = sqlite3.connect("db/elfos.db")
    clientes = pd.read_sql_query("SELECT * from proveidors", conn)
    nombres = clientes["nom"].value_counts()
    nombres.plot(kind="bar")
    plt.show()

def potanalitica():
    conn = sqlite3.connect("db/elfos.db")
    clientes = pd.read_sql_query("SELECT * from clientes_pot", conn)
    nombres = clientes["name"].value_counts()
    nombres.plot(kind="bar")
    plt.show()


