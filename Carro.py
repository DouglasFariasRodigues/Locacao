class Carro:
    def __init__(self, marca, modelo, ano,placa):
        #CONSTRUTOR DAS INFORMÇÕES DO  CARRO
        self._marca = marca
        self._modelo = modelo
        self._ano = ano
        self.placa = placa

    def __str__(self):
        return f"Dados do Carro:\n\nMarca: {self._marca}\nModelo: {self._modelo}\nAno: {self._ano}.\nPlaca: {self.placa}\n"
    
    
