from veiculo import Veiculo
from carro import Carro

veiculo1 = Veiculo('rosa', 'ford', 6, 190)
carro1 = Carro('azul','sandero', 10)
print(veiculo1.tanque)
carro1.abastecer(90)

print(carro1.tanque)