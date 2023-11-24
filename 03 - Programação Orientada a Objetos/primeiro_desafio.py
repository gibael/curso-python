class bicicleta:
    def __init__(self, cor, modelo, ano, valor) -> None:
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def correr(self):
        print("correndo!")

    def buzinar(self):
        print("Buzinando!")

    def parar(self):
        print("Parando!")
        print("parado!")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

b1 = bicicleta("Rosa", "Monark", 2023, 200)
b1.correr()
b1.buzinar()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = bicicleta("Azul", "CALOI", 2015, 100)
b2.correr()
b2.buzinar()
b2.parar()
print(b2.cor, b2.modelo, b2.ano, b2.valor)

