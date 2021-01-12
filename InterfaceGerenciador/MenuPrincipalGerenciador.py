import sqlite3  # importando tabela para usar o banco de dados
from tkinter import *
import tkinter as tk

conn = sqlite3.connect('password.db')  # Atribuindo a variável o conector do banco de dados

cursor = conn.cursor()  # Atribuindo a variável um executavél

# Comando para criar a tabela que portará os dados das entradas caso ela não exista
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
''')


def sair():
    exit()


def callback():
    print('Chamada de retorno')


def get_password(service):  # Atribuindo uma interação ao banco de dado atraves de um def
    cursor.execute(f'''
        SELECT username, password FROM users
        WHERE service = '{service}'
    ''')

    if cursor.rowcount == 0:  # Condição para caso o cadastro procurado não tenha um registro
        print("Serviço não encontrado (use 'l' para verificar os serviços)")
    else:
        for user in cursor.fetchall():
            print(user)


def insert_password(service, username, password):  # Atribuindo uma interação ao banco de dados atraves de um def
    cursor.execute(f'''
         INSERT INTO users (service, username, password)
         VALUES ('{service}', '{username}', '{password}')
    ''')  # Interação com o banco de dados para inserir um novo registro

    conn.commit()


def show_services():  # Comando para mostrar registros já cadastrados no banco de dados
    cursor.execute('''
        SELECT service FROM users;
    ''')
    for service in cursor.fetchall():
        print(service)


janela = Tk()

lbtext = Label(janela, text="***************************************** \n"
                            "* i : Inserir nova entrada              * \n"
                            "* l : Listar entradas salvas          * \n"
                            "* v : Visualizar entradas salvas  * \n"
                            "* s : Sair                                          * \n"
                            "*****************************************   ")
lbtext.place(x=450, y=100)
lbtext.config(font='Arial 25 bold')

btSV = Button(janela, text="Processar")
btSV.place(x=900, y=650, width=200, height=50)
btCN = Button(janela, text="Cancelar")
btCN.place(x=1100, y=650, width=200, height=50)

menu = Menu(janela)
janela.config(menu=menu)
janelasmenu = Menu(menu)
filemenu = Menu(menu)
janelacadaluno = Menu(menu)
menu.add_cascade(label='Arquivos', menu=filemenu)
filemenu.add_command(label="Novo", command=callback)
filemenu.add_command(label='Janelas', command=callback)
janelasmenu.add_command(label='Cadastro', command=filemenu)
janelacadaluno.add_command(label='Cadastro alunos', command=janelasmenu)
filemenu.add_separator()
filemenu.add_command(label='Sair', command=sair)
helpmenu = Menu(menu)
menu.add_cascade(label="Ajuda", menu=helpmenu)
helpmenu.add_command(label="Sobre...", command=callback)


janela.title("Cadastrar Aluno")
janela.geometry("1366x768+200+200")
janela.mainloop()

conn.close()
