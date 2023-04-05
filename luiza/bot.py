
import time
from datetime import date, timedelta
from paciente import Paciente
from medico import Medico
from collections import deque

#fila abstracao polimorfismo


today_date = date.today()
td = timedelta(5)
consulta = today_date + td
cadastro = 0
contador = 0
contadorP = 0

class bcolors:
    Red = '\033[91m'
    Green = '\033[92m'
    Blue = '\033[94m'
    Cyan = '\033[96m'
    White = '\033[97m'
    Yellow = '\033[93m'
    Magenta = '\033[95m'
    Grey = '\033[90m'
    Black = '\033[90m'
    RESET = '\033[0m'  # RESET COLOR

situacoes = {f"{bcolors.Cyan} |1| {bcolors.RESET}": "Carteira de vacinação online", f"{bcolors.Red} |2| {bcolors.RESET}": "Agendar consulta presencial", f"{bcolors.Cyan} |3| {bcolors.RESET}": "Consulta Online Covid19",
             f"{bcolors.Red} |4| {bcolors.RESET}": "Informe os sintômas", f"{bcolors.Cyan} |5| {bcolors.RESET}": 'Perfil do Usuario', f"{bcolors.Red} |6| {bcolors.RESET}": 'Sair do atendimento'}
situacoesMed = f"{bcolors.Cyan} |1| {bcolors.RESET}": 'Consultas agendadas', f"{bcolors.Red} |2| {bcolors.RESET}": 'Escrever Relatório', f"{bcolors.Cyan} |3| {bcolors.RESET}": "Ler Relatorios salvos",
             '|4|': 'Gerar atestado', '|5|': 'Remover Paciente Atendido' , "|6|": "Adicionar Paciente",
                        '|7|': 'Perfil de Usuário', "|8|": "Sair do atendimento"}

fila = (['Ana Lucia Ferreira', 'Biana Moraes Kunicks', 'Carlos Andrade Filho'])

#CÓDIGO

while cadastro != 1 and cadastro != 2:
    print('-=-='* 15)
    cadastro = int(input('\n [1] - Paciente \n [2] - Médico\n Escolha como deseja se cadastrar: '))
    if cadastro != 1 and cadastro != 2:
        print('Resposta inválida!')
    print('-=-=' * 15)

p = Paciente('','','','')
m = Medico('','','','','')

#CADASTRO

if cadastro == 1:
    p.registrar()

    especializacao = 0
elif cadastro == 2:
    m.registrar()

#FUNÇÃO DO PACIENTE

def luizaPaciente():
    print(f"{bcolors.Cyan} Olá, {p.nome} ! Seja Bem-Vindo(a) ao servico de saude automatizada\n {bcolors.RESET} ")
    time.sleep(1)
    print(f"Meu nome é {bcolors.Red}Luiza{bcolors.RESET}")
    time.sleep(1)
    print("Por Favor escolha um de nossos servicos: ")
    time.sleep(1)

def luizaVoltPaciente():
    global contadorP
    for chave, valor in situacoes.items():
        print(chave + " = " + str(valor))

    resposta = input("Qual servico deseja? ")

    if resposta == '1':

        contadorP = 0

        print("Analizando seus dados...")
        time.sleep(2)
        print("...")
        time.sleep(3)
        print("Parabens! Você possui todas as suas vacinas em dia!")
        escolha = input('\nDeseja retornar ao menu? [S/N]\n').strip().upper()
        if escolha == 'S':
            contadorP += 1
        elif escolha == 'N':
            print('Sessão encerrada, até breve!')

    if resposta == '2':

        contadorP = 0

        input("Qual o motivo da consulta?")
        input("\nQual bairro deseja consultar?")
        print("Sua consulta foi agendada para o dia {}!" .format(consulta))
        print("Tenha um bom dia!")
        escolha = input('\nDeseja retornar ao menu? [S/N]\n').strip().upper()
        if escolha == 'S':
            contadorP += 1
        elif escolha == 'N':
            print('Sessão encerrada, até breve!')

    if resposta == '3':

        contadorP = 0

        sintomas = input("Por favor, me conte todos os seus sintomas: ")
        if "Febre, Tosse, Garganta " in (" ".lower() + sintomas + " "):
            print("Uma consulta para um teste rapido em seu posto mais proximo foi marcado para o dia {}" .format(consulta))
        else:
            print("Parece que voce nao possui sintomas de covid19, por favor marque uma consulta com um medico geral")
        escolha = input('\nDeseja retornar ao menu? [S/N]\n').strip().upper()
        if escolha == 'S':
            contadorP += 1
        elif escolha == 'N':
            print('Sessão encerrada, até breve!')

    if resposta == '4':

        contadorP = 0

        quantSintomas = int(input('Informe quantos sintomas você identificou: '))
        sint = []
        for si in range(quantSintomas):
            sint.append(input('Informe o sintôma: '))

        print(f'Os sintomas identificados por você foram:{sint}.')
        print('Estou analisando os dados coletados, logo entrarei em contato novamente te indicando o melhor profissonal!')
        escolha = input('\nDeseja retornar ao menu? [S/N]\n').strip().upper()
        if escolha == 'S':
            contadorP += 1
        elif escolha == 'N':
            print('Sessão encerrada, até breve!')

    if resposta == '5':

        contadorP = 0

        print('-=-=-' * 5 + ' Perfil de Usuário ' + '-=-=-' * 5)
        print(f'Nome Completo: {p.nome}')
        print(f'Idade: {p.idade}')
        print(f'Genêro: {p.genero}')
        print(p.mostrar_informações())
        escolha = input('\nDeseja retornar ao menu? [S/N]\n').strip().upper()
        if escolha == 'S':
            contadorP += 1
        elif escolha == 'N':
            print('Sessão encerrada, até breve!')

    if resposta == '6':
        exit()


#FUNÇÃO MÉDICO
def luizaMedico():
    print("Olá, Dr(a). {} ! Seja Bem-Vindo(a) ao servico de saude automatizada\n" .format(m.nome))
    time.sleep(1)
    print("Meu nome é Luiza")
    time.sleep(1)
    print("Por Favor escolha um de nossos servicos: ")
    time.sleep(1)

def luizaVolt():
    global contador

    for chave, valor in situacoesMed.items():
        print(chave + " = " + str(valor))

    resposta = input("Qual servico deseja? ")

    if resposta == '1':
        contador = 0
        print("Analizando seus dados...")
        time.sleep(2)
        print("...")
        time.sleep(3)
        print("Esse é o total de consultas agendadas para o dia {}" .format(consulta))

        m.listarConsultas()

        escolha = input('\nDeseja retornar ao menu? [S/N]\n').strip().upper()
        if escolha == 'S':
            contador += 1
        elif escolha == 'N':
            print('Sessão encerrada, até breve!')

    if resposta == '2':
        contador = 0

        m.inserirRelatorio()

        escolha = input('\nDeseja retornar ao menu? [S/N]\n').strip().upper()
        if escolha == 'S':
            contador += 1
        elif escolha == 'N':
            print('Sessão encerrada, até breve!')
    if resposta == '3':
        contador = 0

        m.lerRelatorios()

        escolha = input('\nDeseja retornar ao menu? [S/N]\n').strip().upper()
        if escolha == 'S':
            contador += 1
        elif escolha == 'N':
            print('Sessão encerrada, até breve!')

    if resposta == '4':
        contador = 0

        m.gerarAtestado()

        escolha = input('\nDeseja retornar ao menu? [S/N]\n').strip().upper()
        if escolha == 'S':
            contador += 1
        elif escolha == 'N':
            print('Sessão encerrada, até breve!')

    if resposta == '5':
        contador = 0

        fila.pop(0)
        print("A lista de paciente atualizada é: {}" .format(fila))

        escolha = input('\nDeseja retornar ao menu? [S/N]\n').strip().upper()
        if escolha == 'S':
            contador += 1
        elif escolha == 'N':
            print('Sessão encerrada, até breve!')

    if resposta == '6':
        contador = 0

        fila.append(input("Qual o nome completo do paciente: "))
        print("A lista de pacientes atulizada é: {}" .format(fila))

        escolha = input('\nDeseja retornar ao menu? [S/N]\n').strip().upper()
        if escolha == 'S':
            contador += 1
        elif escolha == 'N':
            print('Sessão encerrada, até breve!')
    if resposta == '7':

        contador = 0

        print('-=-=-' * 5 + ' Perfil de Usuário ' + '-=-=-' * 5)
        print(f'Nome Completo: {m.nome}')
        print(f'Idade: {m.idade}')
        print(f'Genêro: {m.genero}')
        print(m.mostrar_informações())

        escolha = input('\nDeseja retornar ao menu? [S/N]\n').strip().upper()
        if escolha == 'S':
            contador += 1
        elif escolha == 'N':
            print('Sessão encerrada, até breve!')

    if resposta == '8':
        exit()

if cadastro == 1:
    luizaPaciente()
    luizaVoltPaciente()
elif cadastro == 2:
    luizaMedico()
    luizaVolt()
while contador == 1:
    luizaVolt()
while contadorP == 1:
    luizaVoltPaciente()
