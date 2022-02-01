from datetime import date

from utils.helper import data_para_str, str_para_date


class Cliente:
    contator: int = 1001

    def __init__(self: object, nome: str, cpf: str, data_nascimento: str) -> None:
        self.__codigo: int = Cliente.contator
        self.__nome: str = nome
        self.__cpf: str = cpf
        self.__data_nascimento: date = str_para_date(data_nascimento)
        self.__data_cadastro: date = date.today()
        Cliente.contator += 1

    @property
    def codigo(self: object) -> str:
        return self.__codigo

    @property
    def nome(self: object) -> str:
        return self.__nome

    @property
    def cpf(self: object) -> str:
        return self.__cpf

    @property
    def data_nascimento(self: object) -> str:
        return data_para_str(self.__data_nascimento)

    @property
    def data_cadastro(self: object) -> str:
        return data_para_str(self.__data_cadastro)

    def __str__(self: object) -> str:
        return f"Código: {self.codigo} \nNome: {self.nome} \nData Nascimento: {self.data_nascimento} \nData Cadastro: {self.data_cadastro}"
