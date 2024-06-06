# Cadastro de funcionários
funcionarios = {}

# Adicionando funcionários
funcionarios["001"] = {"nome": "Ana", "cargo": "Engenheira", "salario": 5000}
funcionarios["002"] = {"nome": "Pedro", "cargo": "Gerente", "salario": 7000}

# Função para adicionar novo funcionário
id_funcionario = "003"
dados_funcionario = {"nome": "Carlos", "cargo": "Analista", "salario": 4000}
if id_funcionario not in funcionarios:
    funcionarios[id_funcionario] = dados_funcionario
    print(f"Funcionário {dados_funcionario['nome']} adicionado com sucesso.")
else:
    print(f"Funcionário com ID {id_funcionario} já existe.")

# Função para atualizar informações de um funcionário
id_atualizar = "001"
if id_atualizar in funcionarios:
    funcionarios[id_atualizar]["salario"] = 5500
    print(f"Salário de {funcionarios[id_atualizar]['nome']} atualizado para {funcionarios[id_atualizar]['salario']}.")
else:
    print(f"Funcionário com ID {id_atualizar} não encontrado.")

# Função para remover um funcionário
id_remover = "002"
if id_remover in funcionarios:
    del funcionarios[id_remover]
    print(f"Funcionário com ID {id_remover} removido com sucesso.")
else:
    print(f"Funcionário com ID {id_remover} não encontrado.")

# Função para visualizar os detalhes de um funcionário
id_pesquisar = "001"
if id_pesquisar in funcionarios:
    print(f"Detalhes do funcionário {id_pesquisar}: {funcionarios[id_pesquisar]}")
else:
    print(f"Funcionário com ID {id_pesquisar} não encontrado.")

# Visualizando todos os funcionários
print("Cadastro de funcionários:", funcionarios)
