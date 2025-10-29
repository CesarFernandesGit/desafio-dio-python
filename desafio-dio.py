menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

opcao_menu = (input(menu))

usuarios = []

def criar_endereco(logradouro, numero, bairro, cidade, sigla, estado):
    return f"{logradouro}, {numero} - {bairro}, {cidade}/{sigla} - {estado}"

usuarios = []

def criar_usuario(nome, email, endereco):
    usuario = {
        "nome": nome,
        "endereco": endereco
    }
    usuarios.append(usuario)
    print(f"Usuário {nome} criado com sucesso!")

endereco_cesar = criar_endereco("Rua das Flores", "123", "Centro", "São Paulo", "SP", "São Paulo")
criar_usuario("César", "28-10-2025", endereco_cesar)

for u in usuarios:
    print(u)

def depositar(valor, /):
    if opcao_menu == "d":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:        
                global saldo, extrato
                saldo += valor
                extrato += f"Depósito: R$ {valor:.2f}\n"    
        else:
            print("Operação falhou! O valor informado é inválido.")
depositar(0)

def sacar():
        if opcao_menu == "s":
            global saldo, numero_saques, LIMITE_SAQUES
            valor = float(input("Informe o valor do saque: "))
            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")

            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")

            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")

            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques += 1

            else:
                print("Operação falhou! O valor informado é inválido.") 
sacar()
