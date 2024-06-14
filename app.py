import itertools
from turmas import Turmas

turno = input('Digite o turno o qual deseja gerar as combinações: ')
serie = input(f'Digite o número da série {turno.lower()}: ')

turnoDict = {'mat': 'matutino',
             'vesp': 'vespertino'}

seriesMap = {
    6: {

    }
}
# Gera as combinacoes possiveis de jogos para cada turma
def geraJogos():

    if turno == turnoDict['mat']:
        if serie == '6':
            Turmas.tSexto = list(itertools.permutations(Turmas.tSexto, 2))
            resultado = Turmas.tSexto
            print(f'Possibilidades: {resultado}')
        else:
            Turmas.tSetimo = list(itertools.permutations(Turmas.tSetimo, 2))
            resultado = Turmas.tSetimo
            print(f'Possibilidades: {resultado}')
    elif turno == turnoDict['vesp']:
        if serie == '8':
            Turmas.tOitavo = list(itertools.permutations(Turmas.tOitavo, 2))
            resultado = Turmas.tOitavo
            print(f'Possibilidades: {resultado}')
        else:
            Turmas.tNono = list(itertools.permutations(Turmas.tNono, 2))
            resultado = Turmas.tNono
            print(f'Possibilidades: {resultado}')
    else:
        print('Erro: Digite corretamente turno e série desejados')

    try:
        resultado
    except:
        print('Erro: Digite corretamente turno e série desejados')


geraJogos()
