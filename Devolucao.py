from Cliente import*
from Carro import*

class Devolucao:
    def __init__(self, contrato,carro=Carro):
        self._contrato = contrato
        self._carro= carro
        
        

    def locacao(self):
        if self._contrato._locacao:
            self._contrato._locacao = False
            print(f"Devolução realizada para {self._contrato._cliente._nome}.")
        else:
            print("Nenhuma locação ativa para este contrato.")

    def reembolso(self, valor):
        if valor <= self._contrato._pagamento:
            self._contrato._pagamento -= valor
            print(f"Reembolso de {valor} realizado para {self._contrato._cliente._nome}.")
        else:
            print("Valor de reembolso excede o valor pago.")

    def __str__(self):
        return f"--------------------------------------------------------------------------------------------------\nContrato de Devolução\n {self._contrato._cliente}\n{self._carro}\n"
