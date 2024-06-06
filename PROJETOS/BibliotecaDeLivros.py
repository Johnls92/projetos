# Biblioteca de livros
biblioteca = {}

# Adicionando livros
biblioteca["1984"] = {"autor": "George Orwell", "ano": 1949, "disponivel": True}
biblioteca["O Senhor dos Anéis"] = {"autor": "J.R.R. Tolkien", "ano": 1954, "disponivel": False}

# Função para adicionar novo livro
titulo_livro = "O Hobbit"
dados_livro = {"autor": "J.R.R. Tolkien", "ano": 1937, "disponivel": True}
if titulo_livro not in biblioteca:
    biblioteca[titulo_livro] = dados_livro
    print(f"Livro '{titulo_livro}' adicionado com sucesso.")
else:
    print(f"Livro '{titulo_livro}' já existe na biblioteca.")

# Função para atualizar informações de um livro
livro_atualizar = "1984"
if livro_atualizar in biblioteca:
    biblioteca[livro_atualizar]["disponivel"] = False
    print(f"Disponibilidade do livro '{livro_atualizar}' atualizada para {biblioteca[livro_atualizar]['disponivel']}.")
else:
    print("Livro não encontrado.")

# Função para remover um livro
livro_remover = "O Senhor dos Anéis"
if livro_remover in biblioteca:
    del biblioteca[livro_remover]
    print(f"Livro '{livro_remover}' removido da biblioteca.")
else:
    print("Livro não encontrado.")

# Função para consultar disponibilidade de um livro
livro_pesquisar = "1984"
if livro_pesquisar in biblioteca:
    print(f"Detalhes do livro '{livro_pesquisar}': {biblioteca[livro_pesquisar]}")
else:
    print("Livro não encontrado.")

# Visualizando a biblioteca completa
print("Biblioteca de livros:", biblioteca)
