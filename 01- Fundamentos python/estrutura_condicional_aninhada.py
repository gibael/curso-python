conta_normal = True
conta_universitaria = True
conta_especial = True

saldo = 2000
saque = float(input("Insira o valor que quer sacar: "))
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque com cheque especial realizado com sucesso!")
    else:
        print("Você não tem saldo suficiente!")
if conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Saldo Insuficiente!")
if conta_especial:
    print("Conta especial Selecionada!")

else:
    print("Sistema não reconheceu seu tipo de conta, favor entrar em contato com Gerente.")