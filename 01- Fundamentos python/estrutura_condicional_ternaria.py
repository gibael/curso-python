saldo = 2000
saque = float(input("Valor que deseja sacar: "))

status = "Sucesso" if saque <= saldo else "Falha"

print (f"{status} ao realizar o saque!")