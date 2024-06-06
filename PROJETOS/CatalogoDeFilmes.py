# Catálogo de filmes
catalogo_filmes = {}

# Adicionando filmes
catalogo_filmes["Inception"] = {"diretor": "Christopher Nolan", "ano": 2010, "genero": "Ficção Científica"}
catalogo_filmes["Matrix"] = {"diretor": "Lana Wachowski, Lilly Wachowski", "ano": 1999, "genero": "Ficção Científica"}

# Função para adicionar novo filme
titulo_filme = "Interstellar"
dados_filme = {"diretor": "Christopher Nolan", "ano": 2014, "genero": "Ficção Científica"}
if titulo_filme not in catalogo_filmes:
    catalogo_filmes[titulo_filme] = dados_filme
    print(f"Filme '{titulo_filme}' adicionado com sucesso.")
else:
    print(f"Filme '{titulo_filme}' já existe no catálogo.")

# Função para atualizar informações de um filme
filme_atualizar = "Inception"
if filme_atualizar in catalogo_filmes:
    catalogo_filmes[filme_atualizar]["ano"] = 2011
    print(f"Ano de lançamento do filme '{filme_atualizar}' atualizado para {catalogo_filmes[filme_atualizar]['ano']}.")
else:
    print("Filme não encontrado.")

# Função para remover um filme
filme_remover = "Matrix"
if filme_remover in catalogo_filmes:
    del catalogo_filmes[filme_remover]
    print(f"Filme '{filme_remover}' removido do catálogo.")
else:
    print("Filme não encontrado.")

# Visualizando o catálogo completo
print("Catálogo de filmes:", catalogo_filmes)
