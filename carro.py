from veiculo import Veiculo

class Carro(Veiculo):

    def __init__(self, cor, marca, tanque):
        Veiculo.__init__(self, cor, 4, marca, tanque)

    def abastecer(self, litros):
        if self.tanque + litros > 50:
            print("Erro: tanque cheio")
        else:
            self.tanque += litros

'''
EXERCICIO : Crie um software de gerenciamneto bancário
Esse softawre poderá ser capaz de criar clientes e contas
Cada cliente possui nome, cpf, idade
Cada conta possui um cliente, saldo, limite, sacar, depositar e consultar saldo.
'''
