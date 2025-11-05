import textwrap


def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

saldo = 0
limite = 500
extrato_bancario = ""
numero_saques = 0
LIMITE_SAQUES = 3

usuarios = []
contas = []

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nConta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\nUsuário não encontrado, fluxo de criação de conta encerrado!")

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

def depositar(valor, saldo, extrato_bancario, /):
    if valor > 0:
        saldo += valor
        extrato_bancario += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato_bancario

def sacar(*, saldo, valor, extrato_bancario, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

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

    return saldo, extrato_bancario


def exibir_extrato(saldo, /, *, extrato_bancario):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato_bancario else extrato_bancario)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

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
