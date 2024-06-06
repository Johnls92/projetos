# Agenda de contatos
agenda = {}

# Adicionando contatos
agenda["João"] = "123456789"
agenda["Maria"] = "987654321"

# Função para adicionar novo contato
nome_contato = "Ana"
telefone_contato = "555123456"
if nome_contato not in agenda:
    agenda[nome_contato] = telefone_contato
    print(f"Contato {nome_contato} adicionado com sucesso.")
else:
    print(f"Contato {nome_contato} já existe.")

# Função para remover contato
nome_remover = "Maria"
if nome_remover in agenda:
    del agenda[nome_remover]
    print(f"Contato {nome_remover} removido com sucesso.")
else:
    print(f"Contato {nome_remover} não encontrado.")

# Função para pesquisar contato
nome_pesquisar = "João"
if nome_pesquisar in agenda:
    print(f"Telefone de {nome_pesquisar}: {agenda[nome_pesquisar]}")
else:
    print(f"Contato {nome_pesquisar} não encontrado.")

# Visualizando a agenda completa
print("Agenda de contatos:", agenda)
