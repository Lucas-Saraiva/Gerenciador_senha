import sqlite3  # importando tabela para usar o banco de dados

MASTER_PASSWORD = "123456"  # atribuindo uma senha master

senha = input("Insira sua senha Master:")   # Input para verificar se o usuario é o certo
if senha != MASTER_PASSWORD:    # Condição para que se a senha for errada derrubar o usuario
    print("Senha Inválida! Encerrando ...")
    exit()

conn = sqlite3.connect('password.db')   # Atribuindo a variável o conector do banco de dados

cursor = conn.cursor()  # Atribuindo a variável um executavél

# Comando para criar a tabela que portará os dados das entradas caso ela não exista
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
''')


def menu():     # Criando menu de interação e o atribuindo a um def
    print("*********************************** \n"
          "* i : Inserir nova entrada        * \n"
          "* l : Listar entradas salvas      * \n"
          "* v : Visualizar entradas salvas  * \n"
          "* s : Sair                        * \n"
          "***********************************   ")


def get_password(service):  # Atribuindo uma interação ao banco de dado atraves de um def
    cursor.execute(f'''
        SELECT username, password FROM users
        WHERE service = '{service}'
    ''')

    if cursor.rowcount == 0:    # Condição para caso o cadastro procurado não tenha um registro
        print("Serviço não encontrado (use 'l' para verificar os serviços)")
    else:
        for user in cursor.fetchall():
            print(user)


def insert_password(service, username, password):   # Atribuindo uma interação ao banco de dados atraves de um def
    cursor.execute(f'''
         INSERT INTO users (service, username, password)
         VALUES ('{service}', '{username}', '{password}')
    ''')    # Interação com o banco de dados para inserir um novo registro

    conn.commit()


def show_services():    # Comando para mostrar registros já cadastrados no banco de dados
    cursor.execute('''
        SELECT service FROM users;
    ''')
    for service in cursor.fetchall():
        print(service)


while True:     # Condição de repetição
    menu()  # Puxando o menu pelo def
    op = input("Operação desejada:")    # Input para saber qual operação deverá ser processado
    if op not in ['i', 'l', 'v', 's']:  # Comando para interver letras não cadastradas no codigo
        print("Opção Inválida!")
        continue

    if op == 's':   # Comando caso 's' seja selecionado
        break

    if op == 'i':   # Comando para cadastrar novas entradas
        service = input("Qual o nome do serviço:")
        username = input("Qual o seu username:")
        password = input(f"Senha do usuário '{username}':")
        insert_password(service, username, password)

    if op == 'l':   # Comando para listar todos os registros cadastrados
        show_services()

    if op == 'v':   # Comando para ver os detalhes do registro
        service = input("De qual entrada será a senha:")
        get_password(service)

conn.close()
