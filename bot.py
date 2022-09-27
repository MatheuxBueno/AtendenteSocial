#• Estruturas básicas do Python (programação estruturada) (2,0);
#• Função (1,5);
#• Recursividade (1,5)
#• Listas (Conjuntos, Dicionários; e/ou Tuplas) (1,5);
#• Pilhas (1,5)#

import time
from datetime import date, timedelta
import dateutil.relativedelta as relativedelta

today_date = date.today()
td = timedelta(5)
consulta = today_date + td

situacoes = {"1": "Carteira de vacinação online", "2": "Agendar consulta presencial", "3": "Consulta Online Covid19",
             "4": "Informe os sintômas", '5': 'Sair do atendimento'}
nome = {}
cpf = {}
print('\nPara iniciar informe seu nome e cpf')
for chave, valor in nome.items():
    print(chave + ' = ' + str(valor))
escolha_nome = str(input('Deseja se cadastrar? [SIM/NAO]: ').upper())
if escolha_nome == 'SIM':
    print('Por favor, insira seus dados')
    nome = input('Nome: ')
    cpf = int(input('\nCPF: '))
    print('\nObrigado pelo cadastro!\n')
elif escolha_nome == 'NAO':
    exit()
elif escolha_nome != 'SIM' and escolha_nome != 'NÃO':
    print('Escolha uma resposta válida. [SIM/NAO]')
    

def start ():

    print("Olá, {} ! Seja Bem-Vindo(a) ao servico de saude automatizada\n" .format(nome))
    time.sleep(1)
    print("Meu nome é Luiza")
    time.sleep(1)
    print("Por Favor escolha um de nossos servicos: ")
    time.sleep(1)

    for chave, valor in situacoes.items():
        print(chave + " = " + str(valor))

    resposta = input("Qual servico deseja? ")

    if resposta == '1':
        print("Analizando seus dados...")
        time.sleep(2)
        print("...")
        time.sleep(3)
        print("Parabens! Você possui todas as suas vacinas em dia!")
    if resposta == '2':
        input("Qual o motivo da consulta?")
        input("\nQual bairro deseja consultar?")
        print("Sua consulta foi agendada para o dia {}!" .format(consulta))
        print("Tenha um bom dia!")
        exit()
    if resposta == '3':
        sintomas = input("Por favor, me conte todos os seus sintomas: ")
        if "Febre, Tosse, Garganta " in (" " + sintomas + " "):
            print("Uma consulta para um teste rapido em seu posto mais proximo foi marcado para o dia {}" .format(consulta))
        else:
            print("Parece que voce nao possui sintomas de covid19, por favor marque uma consulta com um medico geral")
    if resposta == '4':
        quantSintomas = int(input('Informe quantos sintomas você identificou: '))
        sint = []
        for si in range(quantSintomas):
            sint.append(input('Informe o sintôma: '))

        print(f'Os sintomas identificados por você foram:{sint}.')
        print('Estou analisando os dados coletados, logo entrarei em contato novamente te indicando o melhor profissonal!')

    if resposta == '5':
        exit()

if __name__ == '__main__':
    start()
