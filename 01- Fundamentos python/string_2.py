nome = "Gabriel"
idade = "26"
saldo = 12.3456

dados = {"nome": "Gabriel", "idade": 26}

#antigo, muito raro utilizar
print("Nome: %s Idade: %s" % (nome, idade))

#as vezes utiliza
print("Nome: {} Idade: {}".format(nome, idade))

print("Nome: {0} Idade: {1}".format(nome, idade))
print("Nome: {0} Idade: {1} Nome: {0} {0}".format(nome, idade))

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age}".format(name=nome, age=idade))
print("Nome: {nome} Idade: {idade}".format(**dados))

#mais utilizado
print(f"Nome: {nome} idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.3f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.1f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}")