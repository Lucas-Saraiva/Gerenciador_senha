import sqlite3
from tkinter import *

conn = sqlite3.connect('password.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
''')


def show_service():
    cursor.execute('''
        SELECT service FROM users;
    ''')
    for service in cursor.fetchall():
        print(service)
    SS = Label(janela, service)
    SS.place(x=15, y=300)


def btEXECUTE_click():
    print("Salvo")
    show_service


janela = Tk()

lbservices = Label(janela, text="Serviços:")
lbservices.place(x=15, y=200)
lbservices.config(font="Arial 20")

btEX = Button(janela, text="EXECUTAR", command=btEXECUTE_click)
btEX.place(x=950, y=650, width=200, height=50)

janela.title("Menu Serviços")
janela.geometry("1366x768+200+200")
janela.mainloop()
