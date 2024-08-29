#IMPORTAÇÃO DAS CLASSES
from Cliente import*
from Carro import*
from Devolucao import*
from Contrato import*

#CRIAÇÃO DO CLIENTE
cliente1 = Cliente("Carlos", 12345678910, 8799123545)

#CRIAÇÃO DO CARRO
carro=Carro("FIAT","UNO",2003,"UHF3945")

#CRIAÇÃO DO CONTRATO
contrato1 = Contrato(cliente1, False, 1000, carro)

#CRIAÇÃO DO CONTRATO DE DEVOLUÇÃO
devolucao1 = Devolucao(contrato1,carro)

#IMPRESSÕES
print(cliente1)
print(contrato1)
print(devolucao1)