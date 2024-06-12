import random
import itertools
from turmas import Turmas

turno = input('Digite o turno o qual deseja gerar as combinações: ')
serie = input(f'Digite a série das turmas do perído {turno.lower()}: ')
turmas_mat = ['6A', '6B', '7A', '7B']
turmas_vesp = ['8A', '8B', '9A', '9B']

# Gera as combinacoes possiveis de jogos para cada turma
def combinacao():

    if turno == 'matutino' or turno == 'Matutino' or turno == 'MATUTINO':
        combinacao_mat = list(itertools.combinations(turmas_mat, 2))
        print(f"Primeiro Turno: {combinacao_mat}")
    elif turno == 'vespertino' or turno == 'VESPERTINO' or turno == 'Vespertino':
        combinacao_vesp = list(itertools.combinations(turmas_vesp, 2))
        print(f"Primeiro Turnooo: {combinacao_vesp}")
    else:
        print('Erro: digite corretamente o turno desejado.')


    return


combinacao()
