from abc import ABC, abstractmethod
class Pessoa():
    def __init__(self, nome, idade, genero, cpf):
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.cpf = cpf

    @abstractmethod
    def registrar(self):
        pass

    @abstractmethod
    def mostrar_informações(self):
        pass
