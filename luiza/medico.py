#Info Medico
from pessoa import Pessoa
class Medico(Pessoa):
    def __init__(self,nome, idade, genero, cpf, especializacao):
        super().__init__(nome, idade, genero, cpf)
        self.__especializacao = especializacao

    def registrar(self):
        print('Por favor, insira seus dados')
        self.nome = input('Nome: ')
        self.idade = int(input('Idade: '))
        self.genero = str(input('Genêro: '))
        self.__cpf = int(input('CPF: '))
        self.__especializacao = input('Especialização: ')
        print('\nObrigado pelo cadastro!\n')

    def listarConsultas(self):
        with open("consultas.txt", 'w') as arquivo:
            horarios = arquivo.write('                      CONSULTAS AGENDADAS    \n'
                                     '| Teresinha dos Santos Barboza - 15:20 |  \n'
                                     '| Lucas Dos Santos - 15:50 |   \n'
                                     '| Amelia Aparecida Jose - 16:20 |  \n'
                                     '| Ines Oliveira  - 17:20 |  \n'
                                     '| Joaquim Snheski Junior - 17:50 |  \n'
                                     '| Andre Batista Freire - 18:25 |        \n')

        with open("consultas.txt", "r") as arquivo:
            horarios = arquivo.read()
        print(horarios)

    def inserirRelatorio(self):
        with open("relatorios.txt", 'w') as arquivo:
            relatorio = arquivo.write('            RELATORIO MÉDICO          \n')

        with open("relatorios.txt", "a") as arquivo:
            relatorio = arquivo.write(input("Qual o relatorio de hoje: \n"))
        print("Relatorio adicionado!")

    def lerRelatorios(self):
        with open("relatorios.txt", "r") as arquivo:
            relatorio = arquivo.read()
            print(relatorio)

    def gerarAtestado(self):
        with open("atestado.txt", "w") as arquivo:
            arquivo.write('                                ATESTADO MEDICO                       \n'
                          'Atesto, para os devidos fins, a pedido do interessado,que _____________\n'
                          'portador do RG:_____________, foi submetido a consulta medica nesta data,\n'
                          'no horario das ____________ sendo portador da afeccao CID - 10 _____________.\n'
                          'Em decorrencia, devera permanecer afastado de suas atividades laborativas por um periodo\n'
                          'de __________ (____________) dias, a partir desta data.\n'
                          '                              ASSINATURA DO MEDICO                       \n'
                          '                              ______________________                   \n')
        with open('atestado.txt', 'r') as arquivo:
            atestado = arquivo.read()
        print(atestado)

    def mostrar_informações(self):
        return f'CPF: {self.__cpf}' + f'\nEspecilização: {self.__especializacao}'