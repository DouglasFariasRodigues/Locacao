class Cliente:
    def __init__(self, nome, cpf, telefone):
        self._nome = nome
        self._cpf = cpf
        self._telefone = telefone

    def __str__(self):
        return f"--------------------------------------------------------------------------------------------------\nDados do Cliente:\n\nCliente: {self._nome}\nCPF: {self._cpf}\nTelefone: {self._telefone}.\n--------------------------------------------------------------------------------------------------\n "




