class Veiculo:
    def __init__ (self, modelo, ano, preço):
        self.modelo = modelo
        self.ano = ano 
        self.preço = preço 
    
    def calcular_imposto(self):
        return self.preço * 0.10 

class Carro(Veiculo):
    def __init__(self, modelo, ano, preço, marca):
        super().__init__(modelo, ano, preço)
        self.marca = marca
    
    def desconto(self):
        return self.preço * 0.05

class Moto(Veiculo):
    def __init__(self, modelo, ano, preço, cilindrada):
        super().__init__(modelo, ano, preço)
        self.cilindrada = cilindrada
    
    def calcular_imposto(self):
        return self.preço * 0.05


carro1 = Carro(
    modelo="Civic",
    ano=2022,
    preço=120000.00,
    marca="Honda"
)


moto1 = Moto(
    modelo="CB 500",
    ano=2021,
    preço=40000.00,
    cilindrada=500
)

print("=== CARRO ===")
print("Modelo:", carro1.modelo)
print("Marca:", carro1.marca)
print("Ano:", carro1.ano)
print("Preço: R$", carro1.preço)

print("Imposto: R$", carro1.calcular_imposto())
print("Desconto: R$", carro1.desconto())


print("=== MOTO ===")
print("Modelo:", moto1.modelo)
print("Cilindrada:", moto1.cilindrada, "cc")
print("Ano:", moto1.ano)
print("Preço: R$", moto1.preço)

print("Imposto: R$", moto1.calcular_imposto())
