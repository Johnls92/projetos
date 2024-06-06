# Gestão de estoque
estoque = {}

# Adicionando produtos
estoque["Notebook"] = 10
estoque["Smartphone"] = 20

# Função para adicionar novo produto
nome_produto = "Tablet"
quantidade_produto = 15
if nome_produto not in estoque:
    estoque[nome_produto] = quantidade_produto
    print(f"Produto {nome_produto} adicionado com sucesso.")
else:
    print(f"Produto {nome_produto} já existe.")

# Função para atualizar a quantidade de um produto
produto_atualizar = "Notebook"
nova_quantidade = 5
if produto_atualizar in estoque:
    estoque[produto_atualizar] += nova_quantidade
    print(f"Quantidade de {produto_atualizar} atualizada para {estoque[produto_atualizar]}.")
else:
    print(f"Produto {produto_atualizar} não encontrado.")

# Função para remover um produto
produto_remover = "Smartphone"
if produto_remover in estoque:
    del estoque[produto_remover]
    print(f"Produto {produto_remover} removido com sucesso.")
else:
    print(f"Produto {produto_remover} não encontrado.")

# Visualizando o estoque atual
print("Estoque atual:", estoque)
