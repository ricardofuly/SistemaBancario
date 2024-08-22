menu = """

Escolha uma opção:

[1] Deposito
[2] Saque
[3] Extrato Bancário
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def deposito(deposito_valor, conta_saldo, conta_extrato):
    if deposito_valor > 0:
        conta_saldo += deposito_valor
        conta_extrato += f"Depósito: R$ {deposito_valor:.2f}\n"
        print(f"Depósito de R$ {deposito_valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! o valor informado é invalido.")
    return conta_saldo, conta_extrato
        
def saque(saque_valor, conta_limite, conta_saldo, conta_extrato, num_saques, limite_saques):
    excedeu_saldo = saque_valor > conta_saldo
    exedeu_limite = saque_valor > conta_limite
    exedeu_saques = num_saques >= limite_saques
    
    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente")
    elif exedeu_limite:
        print("Operação falhou! O valor do saque excedeu o limite.")
    elif exedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif saque_valor > 0:
        conta_saldo -= saque_valor
        conta_extrato += f"Saque: R$ {saque_valor:.2f}\n"
        num_saques += 1
        print(f"Saque de R$ {saque_valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é invalido.")
    return conta_saldo, conta_extrato, num_saques
        
def verifica_extrato(conta_extrato, conta_saldo):
    print("\n================= EXTRATO ==================")
    print("Não foram realizadas movimentações." if not conta_extrato else conta_extrato)
    print(f"\nSaldo: R$ {conta_saldo:.2f}")
    print("==============================================")      
    
    
while True:
    opcao = input(menu)
    
    if opcao == "1":
        valor = float(input("Informe o valor de deposito: "))
        saldo, extrato = deposito(valor, saldo, extrato)
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = saque(valor, limite, saldo, extrato, numero_saques, LIMITE_SAQUES)
    elif opcao == "3":
        verifica_extrato(extrato, saldo)
    elif opcao == "4":
        break
    else:
        print("Operação invalida, por favor selecione novamente a opção desejada.")