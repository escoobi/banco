from typing import List
from time import sleep
from models.conta import Conta
from models.cliente import Cliente

contas: List[Conta] = []


def main() -> None:
    menu()


def menu() -> None:
    print("-" * 100)
    print(" " * 40 + " Caixa Eletronico")
    print("-" * 100)
    print("Selecionar uma opção: ")
    print("1 - Criar Conta: ")
    print("2 - Saque: ")
    print("3 - Deposito: ")
    print("4 - Transferencia: ")
    print("5 - Listar Conta: ")
    print("6 - Sair: ")
    opcao: int = int(input())
    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print("Bye!")
        sleep(2)
        exit(0)
    else:
        print("Opção inválida.")
        sleep(2)
        menu()


def criar_conta() -> None:
    print("Informe os dados do cliente: ")
    nome: str = str(input("Nome do cliente: "))
    cpf: str = str(input("CPF do cliente: "))
    data_nascimento: str = str(input("Data Nascimento do cliente: "))

    cliente: Cliente = Cliente(nome, cpf, data_nascimento)
    conta: Conta = Conta(cliente)
    contas.append(conta)

    print("Conta criada com sucesso!")
    print("Dados da conta")
    print("-")
    print(conta)
    sleep(2)
    menu()


def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input("Informe o numero da conta: "))
        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input("Informa o valor do saque: "))
            conta.sacar(valor)
            sleep(2)
            menu()
        else:
            print(f"Conta {numero} não localizada.")
            sleep(2)
            menu()
    else:
        print("Não existe conta cadastrada.")
        sleep(2)
        menu()


def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input("Informe o numero da conta: "))
        conta: Conta = buscar_conta_por_numero(numero)
        if conta:
            valor: float = float(input("Informe o valor: "))
            conta.depositar(valor)
            sleep(2)
            menu()
        else:
            print(f"Conta {numero} não localizada.")
            sleep(2)
            menu()

    else:
        print("Não existe conta cadastrada.")
        sleep(2)
        menu()


def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero_o: int = int(input("Informe o numero da conta: "))
        conta_o: Conta = buscar_conta_por_numero(numero_o)

        if conta_o:
            numero_d: int = int(input("Informe o numero destino: "))
            conta_d: Conta = buscar_conta_por_numero(numero_d)

            if conta_d:
                valor: float = float(input("Informa o valor da transferencia: "))
                conta_o.transferir(conta_d, valor)
                sleep(2)
                menu()
            else:
                print(f"Conta {numero_d} não localizada.")
                sleep(2)
                menu()
        else:
            print(f"Conta {numero_o} não localizada.")
            sleep(2)
            menu()
    else:
        print("Não existe conta cadastrada.")
        sleep(2)
        menu()


def listar_contas() -> None:
    if len(contas) > 0:
        print("Lista de contas: ")
        for ct in contas:
            print(ct)
            print("--------------")
            sleep(1)
            menu()

    else:
        print("Não existe conta cadastrada.")
        sleep(2)
        menu()


def buscar_conta_por_numero(numero: int) -> Conta:

    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c


if __name__ == "__main__":
    menu()
