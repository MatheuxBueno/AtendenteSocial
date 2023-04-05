from pessoa import Pessoa

class Paciente(Pessoa):
    def __init__(self, nome, idade, genero, cpf):
        super().__init__(nome, idade, genero, cpf)

    def registrar(self):
        print('Por favor, insira seus dados')
        self.nome = input('Nome: ')
        self.idade = int(input('Idade: '))
        self.genero = str(input('Genêro: '))
        self.__cpf = int(input('CPF: '))
        print('\nObrigado pelo cadastro!\n')

    def mostrar_informações(self,):
        return f'CPF: {self.__cpf}'



