menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato_bancario = ""
numero_saques = 0
LIMITE_SAQUES = 3

usuarios = []
contas = []

def criar_endereco(logradouro, numero, bairro, cidade, sigla, estado):
    return f"{logradouro}, {numero} - {bairro}, {cidade}/{sigla} - {estado}"

def criar_usuario(nome, cpf, endereco):
    usuario = {
        "nome": nome,
        "cpf": cpf,
        "endereco": endereco
    }
    usuarios.append(usuario)
    print(f"Usuário {nome} criado com sucesso!")

def criar_conta_corrente(cpf, usuarios, contas):
    usuario = next((u for u in usuarios if u["cpf"] == cpf), None)

    if not usuario:
        print("Usuário não encontrado. Verifique o CPF informado.")
        return
    
    numero_conta = len(contas) + 1
    conta = {
        "agencia": "0001",
        "numero_conta": numero_conta,
        "usuario": usuario
    }

    contas.append(conta)
    print(f"Conta {numero_conta} criada com sucesso para {usuario['nome']}!")

def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
        return

    for conta in contas:
        print(f"""
        Agência: {conta['agencia']}
        Conta: {conta['numero_conta']}
        Titular: {conta['usuario']['nome']}
        CPF: {conta['usuario']['cpf']}
        """)

def depositar(valor, /):
    global saldo, extrato_bancario
    if valor > 0:
        saldo += valor
        extrato_bancario += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

def sacar(*, valor):
    global saldo, numero_saques, extrato_bancario

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite de R$ 500,00.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques diários excedido (3 por dia).")

    elif valor > 0:
        saldo -= valor
        extrato_bancario += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso! ({numero_saques}/3 saques do dia)")

    else:
        print("Operação falhou! O valor informado é inválido.") 

def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

endereco_cesar = criar_endereco("Rua das Flores", "123", "Centro", "São Paulo", "SP", "São Paulo")
criar_usuario("César", "12345678900", endereco_cesar)
criar_conta_corrente("12345678900", usuarios, contas)

while True:
    opcao_menu = input(menu)

    if opcao_menu == "d":
        valor = float(input("Informe o valor do depósito: "))
        depositar(valor)

    elif opcao_menu == "s":
        valor = float(input("Informe o valor do saque: "))
        sacar(valor=valor)

    elif opcao_menu == "e":
        exibir_extrato(saldo, extrato=extrato_bancario)

    elif opcao_menu == "q":
        print("Saindo do sistema...")
        break

    else:
        print("Operação inválida, por favor selecione novamente.")
