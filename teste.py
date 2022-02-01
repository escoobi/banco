from models.cliente import Cliente
from models.conta import Conta

gustavo: Cliente = Cliente("Gustavo", "810.666.432-53", "07/10/1985")

contaa: Conta = Conta(gustavo)

