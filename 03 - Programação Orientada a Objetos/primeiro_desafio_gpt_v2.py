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

    def __str__(self):
        return f"Bicicleta {self.modelo} ({self.ano}), cor {self.cor}, status: {self.status}, valor: R${self.valor:.2f}"

if __name__ == "__main__":
    bicicleta1 = Bicicleta("Verde", "Mountain Bike", 2022, 500.00)
    bicicleta2 = Bicicleta("Azul", "Speed", 2021, 700.00)

    print(bicicleta1)
    print(bicicleta2)

    bicicleta1.correr()
    bicicleta1.buzinar()
    bicicleta1.parar()

    bicicleta2.parar()
    bicicleta2.correr()
    bicicleta2.buzinar()
