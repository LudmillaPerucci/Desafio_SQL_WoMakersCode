import sqlite3 

conexao = sqlite3.connect('desafio')

dados = conexao.cursor()

# 1. Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto).

# dados.execute('CREATE TABLE alunos (id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100));')

# 2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.

# dados.execute('INSERT INTO alunos(id,nome, idade,curso) VALUES (1,"Isadora",20, "Ciência de Dados" )')
# dados.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (2, "Gabriel", 22, "Engenharia de Software")')
# dados.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (3, "Mariana", 21, "Análise e Desenvolvimento de Sistemas")')
# dados.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (4, "Ricardo", 23, "Banco de Dados")')
# dados.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (5, "Camila", 20, "Segurança da Informação")')
# dados.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (6, "Lucas", 24, "Inteligência Artificial")')
# dados.execute('INSERT INTO alunos(nome, idade, curso) VALUES (7,"Fernanda", 25, "Engenharia de Computação")')
# dados.execute('INSERT INTO alunos(nome, idade, curso) VALUES (8,"Rafael", 30, "Engenharia Elétrica")')
# dados.execute('INSERT INTO alunos(nome, idade, curso) VALUES (9,"Bruna", 33, "Engenharia Mecatrônica")')


# 3. Consultas Básicas Escreva consultas SQL para realizar as seguintes tarefas:


# a) Selecionar todos os registros da tabela "alunos".
# visualizar = dados.execute('SELECT * FROM alunos')
# for usuario in dados:
#     print(usuario)

# b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
# visualizar = dados.execute('SELECT nome,idade FROM alunos WHERE idade >20')
# for usuario in dados:
#     print(f'{usuario[0]} tem {usuario[1]} anos')

# c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
# visualizar = dados.execute('SELECT nome,curso FROM alunos WHERE curso LIKE "%Engenharia%" ORDER BY nome ASC')
# for usuario in visualizar:
#     print(f'{usuario[0]} cursa {usuario[1]}')

# d) Contar o número total de alunos na tabela
# visualizar = dados.execute('SELECT COUNT(*) FROM alunos')
# for resultado in visualizar:
#     print(f'Total de alunos: {resultado[0]}')

# 4. Atualização e Remoção

# a) Atualize a idade de um aluno específico na tabela.
# dados.execute('UPDATE alunos SET idade = 28 WHERE nome = "Camila"')
# visualizar = dados.execute('SELECT * FROM alunos WHERE nome = "Camila"')
# for usuario in visualizar:
#     print(f'A idade de {usuario[1]} foi atualizada para {usuario[2]} anos.')

# # b) Remova um aluno pelo seu ID.
# dados.execute('DELETE FROM alunos WHERE id = 2')
# print("Aluno com ID 2 removido com sucesso!")

# 5. Criar uma Tabela e Inserir Dados

# Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns registros de clientes na tabela.

#CRIANDO A TABELA CLIENTES
# dados.execute('CREATE TABLE clientes (id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT);')

#INSERINDO REGISTROS
# dados.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (1, "João", 30, 1500.50)')
# dados.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (2, "Maria", 25, 2000.75)')
# dados.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (3, "Carlos", 40, 1200.30)')
# dados.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (4, "Ana", 35, 1800.60)')
# dados.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (5, "Pedro", 28, 2200.90)')
# dados.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (6, "Julia", 32, 2500.40)')
# dados.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (7, "Ricardo", 45, 3000.80)')
# dados.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (8, "Fernanda", 38, 2800.25)')

# visualizar = dados.execute('SELECT * FROM clientes')
# for clientes in dados:
#     print(clientes)


# 6. Consultas e Funções Agregadas Escreva consultas SQL para realizar as seguintes tarefas:

# a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
# visualizar = dados.execute('SELECT nome,idade FROM clientes WHERE idade >30 ORDER BY nome ASC')
# for clientes in dados:
#     print(f'{clientes[0]} tem {clientes[1]} anos')

# b) Calcule o saldo médio dos clientes.
# visualizar = dados.execute('SELECT AVG(saldo) AS saldo_medio FROM clientes')
# for resultado in visualizar:
#     print(f'O saldo médio dos clientes é: {resultado[0]:.2f}')


# c) Encontre o cliente com o saldo máximo.
# visualizar = dados.execute('SELECT nome, saldo FROM clientes WHERE saldo = (SELECT MAX(saldo) FROM clientes)')
# for cliente in visualizar:
#     print(f'O cliente com maior saldo é: {cliente[0]} \nO saldo é: {cliente[1]:.2f}')

# d) Conte quantos clientes têm saldo acima de 1000
# Selecionando os clientes com saldo acima de 1000 e ordenando por saldo
# visualizar = dados.execute('SELECT nome, saldo FROM clientes WHERE saldo > 1000 ORDER BY saldo')

# #  Exibindo os clientes com saldo acima de 1000
# for cliente in visualizar:
#     print(f'O saldo de {cliente[0]} é {cliente[1]:.2f}')

# # Contando o número de clientes com saldo acima de 1000
# visualizar = dados.execute('SELECT COUNT(*) AS clientes_acima_1000 FROM clientes WHERE saldo > 1000')

# # Exibindo o número total de clientes com saldo acima de 1000
# for resultado in visualizar:
#     print(f'\nNúmero total de clientes com saldo acima de 1000: {resultado[0]}')

#7. Atualização e Remoção com Condições
# a) Atualize o saldo de um cliente específico.

# dados.execute('UPDATE clientes SET saldo = 4321 WHERE id = 3')
# conexao.commit()

# visualizar = dados.execute('SELECT nome, saldo FROM clientes WHERE id = 3')
# for cliente in visualizar:
#     print(f'O saldo de {cliente[0]} foi atualizado para: R$ {cliente[1]:.2f}')

# b) Remova um cliente pelo seu ID.
# dados.execute('DELETE FROM clientes WHERE id = 5')
# conexao.commit()

# visualizar = dados.execute('SELECT * FROM clientes')
# for clientes in dados:
#     print(clientes)



#8. Junção de Tabelas
# Crie uma segunda tabela chamada "compras" com os campos: id
# (chave primária), cliente_id (chave estrangeira referenciando o id
# da tabela "clientes"), produto (texto) e valor (real). Insira algumas
# compras associadas a clientes existentes na tabela "clientes".
# Escreva uma consulta para exibir o nome do cliente, o produto e o
# valor de cada compra.

# dados.execute('''CREATE TABLE compras (id INT PRIMARY KEY, cliente_id INT, produto VARCHAR(100), valor FLOAT, FOREIGN KEY(cliente_id) REFERENCES clientes(id))''')
# conexao.commit()

# dados.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES (1, "Smartphone", 1200.50)')
# dados.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES (2, "Laptop", 3200.00)')
# dados.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES (3, "Fone de Ouvido", 350.75)')
# dados.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES (4, "Tablet", 800.90)')
# dados.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES (1, "Capa de Celular", 50.00)')
# dados.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES (2, "Mouse Gamer", 150.00)')
# dados.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES (3, "Carregador Portátil", 120.00)')
# dados.execute('INSERT INTO compras(cliente_id, produto, valor) VALUES (4, "Teclado Bluetooth", 200.00)')
# conexao.commit()


# visualizar = dados.execute('''SELECT clientes.nome, compras.produto, compras.valor FROM compras INNER JOIN clientes ON compras.cliente_id = clientes.id''')

# compras_por_cliente = {}

# for compra in visualizar:
#     nome_cliente, produto, valor = compra
#     if nome_cliente not in compras_por_cliente:
#         compras_por_cliente[nome_cliente] = []
#     compras_por_cliente[nome_cliente].append((produto, valor))

# print("\n--- Compras Realizadas ---\n")
# for cliente, compras in compras_por_cliente.items():
#     total = sum(valor for _, valor in compras)
#     print(f"Cliente: {cliente}")
#     for produto, valor in compras:
#         print(f"  - Produto: {produto} | Valor: R$ {valor:.2f}")
#     print(f"Total: R$ {total:.2f}")
#     print("-" * 40)


conexao.close