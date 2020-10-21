import sqlite3
from tkinter import *

conn = sqlite3.connect('password.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NUll
);
''')


def insert_password(service, username, password):
    cursor.execute(f'''
        INSERT INTO users (service, username, password)
        VALUES ('{service}', '{username}', '{password}')
    ''')

    conn.commit()


def btSV_click():
    print("Salvo")
    insert_password


def btCN_click():
    print("Cancelar")
    exit()


janela = Tk()

service = Entry(janela)
service.place(x=200, y=300, width=200, height=30)
lbservice = Label(janela, text="Serviço")
lbservice.place(x=15, y=300)
lbservice.config(font="Arial 15")

username = Entry(janela)
username.place(x=200, y=350, width=200, height=30)
lbusername = Label(janela, text="Usuário")
lbusername.place(x=15, y=350)
lbusername.config(font="Arial 15")

password = Entry(janela)
password.place(x=200, y=400, width=200, height=30)
lbpassword = Label(janela, text="Senha")
lbpassword.place(x=15, y=400)
lbpassword.config(font="Arial 15")

btSV = Button(janela, text="Salvar", command=btSV_click)
btSV.place(x=950, y=650, width=200, height=50)
btCN = Button(janela, text="Cancelar", command=btCN_click)
btCN.place(x=1150, y=650, width=200, height=50)


janela.title("Cadastro de Entradas")
janela.geometry("1366x768+200+200")
janela.mainloop()
