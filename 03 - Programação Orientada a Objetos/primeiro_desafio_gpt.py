class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.status = "Parada"

    def buzinar(self):
        print(f"A bicicleta {self.modelo} está buzinando.")

    def parar(self):
        self.status = "Parada"
        print(f"A bicicleta {self.modelo} parou.")

    def correr(self):
        if self.status == "Parada":
            self.status = "Em movimento"
            print(f"A bicicleta {self.modelo} começou a correr.")
        else:
            print(f"A bicicleta {self.modelo} já está em movimento.")

if __name__ == "__main__":
    # Exemplo de uso
    bicicleta1 = Bicicleta("Verde", "Mountain Bike", 2022, 500.00)
    bicicleta2 = Bicicleta("Azul", "Speed", 2021, 700.00)

    print("Informações da Bicicleta 1:")
    print(f"Cor: {bicicleta1.cor}")
    print(f"Modelo: {bicicleta1.modelo}")
    print(f"Ano: {bicicleta1.ano}")
    print(f"Valor: R${bicicleta1.valor:.2f}")

    bicicleta1.correr()
    bicicleta1.buzinar()
    bicicleta1.parar()

    print("\nInformações da Bicicleta 2:")
    print(f"Cor: {bicicleta2.cor}")
    print(f"Modelo: {bicicleta2.modelo}")
    print(f"Ano: {bicicleta2.ano}")
    print(f"Valor: R${bicicleta2.valor:.2f}")

    bicicleta2.correr()
    bicicleta2.buzinar()
    bicicleta2.parar()