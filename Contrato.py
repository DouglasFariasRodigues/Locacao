from Carro import*

class Contrato:
    def __init__(self, cliente, locacao=False, pagamento=0.0, carro=Carro):
        self._cliente = cliente
        self._locacao = locacao
        self._pagamento = pagamento
        self._carro = carro

    def realizar_locacao(self):
        self._locacao = True

    def realizar_pagamento(self, valor):
        self._pagamento += valor

    def __str__(self):
        return f"--------------------------------------------------------------------------------------------------\nContrato de Locação\n\nContrato com {self._cliente._nome}\nLocação ativa: {self._locacao}\nPagamento: {self._pagamento}\n{self._carro}\n--------------------------------------------------------------------------------------------------\n"
