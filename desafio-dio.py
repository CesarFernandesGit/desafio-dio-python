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

if opcao_menu == "d":
    
    def depositar(valor, /):
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:        
                global saldo
                saldo += valor
                global extrato
                extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

depositar(0)
    
