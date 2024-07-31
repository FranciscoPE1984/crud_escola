import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="fnlj1984",
    database="escola"
)
cursor = conn.cursor()

def criar_professor(nome):
    sql = "INSERT INTO professores (nome) VALUES (%s)"
    val = (nome,)
    cursor.execute(sql, val)
    conn.commit()
    print(f"Professor '{nome}' criado com sucesso.")

def ler_professores():
    cursor.execute("SELECT * FROM professores")
    resultado = cursor.fetchall()
    for linha in resultado:
        print(linha)

def atualizar_professor(id, novo_nome):
    sql = "UPDATE professores SET nome = %s WHERE id = %s"
    val = (novo_nome, id)
    cursor.execute(sql, val)
    conn.commit()
    print(f"Professor com ID {id} atualizado para '{novo_nome}'.")

def deletar_professor(id):
    sql = "DELETE FROM professores WHERE id = %s"
    val = (id,)
    cursor.execute(sql, val)
    conn.commit()
    print(f"Professor com ID {id} deletado.")

def criar_aluno(nome, nota, frequencia, professor_id):
    sql = "INSERT INTO alunos (nome, nota, frequencia, professor_id) VALUES (%s, %s, %s, %s)"
    val = (nome, nota, frequencia, professor_id)
    cursor.execute(sql, val)
    conn.commit()
    print(f"Aluno '{nome}' criado com sucesso.")

def ler_alunos():
    cursor.execute("SELECT * FROM alunos")
    resultado = cursor.fetchall()
    for linha in resultado:
        print(linha)

def atualizar_aluno_nome(id, novo_nome):
    sql = "UPDATE alunos SET nome = %s WHERE id = %s"
    val = (novo_nome, id)
    cursor.execute(sql, val)
    conn.commit()
    print(f"Nome do aluno com ID {id} atualizado para '{novo_nome}'.")

def atualizar_nota_aluno(id, nova_nota):
    sql = "UPDATE alunos SET nota = %s WHERE id = %s"
    val = (nova_nota, id)
    cursor.execute(sql, val)
    conn.commit()
    print(f"Nota do aluno com ID {id} atualizada para '{nova_nota}'.")

def deletar_aluno(id):
    sql = "DELETE FROM alunos WHERE id = %s"
    val = (id,)
    cursor.execute(sql, val)
    conn.commit()
    print(f"Aluno com ID {id} deletado.")

def menu():
    while True:
        print("\nMenu:")
        print("1. Cadastrar Professor")
        print("2. Listar Professores")
        print("3. Atualizar Professor")
        print("4. Deletar Professor")
        print("5. Cadastrar Aluno")
        print("6. Listar Alunos")
        print("7. Atualizar Nome do Aluno")
        print("8. Atualizar Nota do Aluno")
        print("9. Deletar Aluno")
        print("10. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            nome = input("Digite o nome do professor: ")
            criar_professor(nome)
        elif escolha == '2':
            ler_professores()
        elif escolha == '3':
            id = int(input("Digite o ID do professor: "))
            novo_nome = input("Digite o novo nome do professor: ")
            atualizar_professor(id, novo_nome)
        elif escolha == '4':
            id = int(input("Digite o ID do professor: "))
            deletar_professor(id)
        elif escolha == '5':
            nome = input("Digite o nome do aluno: ")
            nota = float(input("Digite a nota do aluno: "))
            frequencia = float(input("Digite a frequência do aluno: "))
            professor_id = int(input("Digite o ID do professor: "))
            criar_aluno(nome, nota, frequencia, professor_id)
        elif escolha == '6':
            ler_alunos()
        elif escolha == '7':
            id = int(input("Digite o ID do aluno: "))
            novo_nome = input("Digite o novo nome do aluno: ")
            atualizar_aluno_nome(id, novo_nome)
        elif escolha == '8':
            id = int(input("Digite o ID do aluno: "))
            nova_nota = float(input("Digite a nova nota do aluno: "))
            atualizar_nota_aluno(id, nova_nota)
        elif escolha == '9':
            id = int(input("Digite o ID do aluno: "))
            deletar_aluno(id)
        elif escolha == '10':
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()

cursor.close()
conn.close()
