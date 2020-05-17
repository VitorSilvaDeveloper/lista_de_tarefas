import json

def linha():
    print('-'*50)


def tabela():
    print(
    '''
    PARA A LISTA SER SALVA FECHE O PROGRAMA USANDO O 4

    [1] | adicionar tarefa
    [2] | listar tarefa
    [3] | desfazer a ultima tarefa
    [4] | sair
    '''
    )


def desfazer(indice):
    lista_de_tarefas.pop(-1)
    return indice


lista_de_tarefas = []

while True:
    linha()
    tabela()
    linha()

    try:
        opcao = int(input('Digite o que quer fazer: '))
        if opcao == 1:
            linha()
            tarefa = str(input('Qual tarefa deseja adicionar: '))
            lista_de_tarefas.append(tarefa)
            print('Tarefa adicionada')
            linha()

        elif opcao == 2:
            try:
                arquivo_C_lista = 'lista_de_tarefas.json'
                with open(arquivo_C_lista) as arquivo_salvo:
                    lista_de_tarefas = json.load(arquivo_salvo)
                    print(lista_de_tarefas)
            except:
                linha()
                print(lista_de_tarefas)
                linha()

        elif opcao == 3:
            try:
                desfazer(lista_de_tarefas)
                print(lista_de_tarefas)
            except IndexError:
                print('Lista vazia, tem que adiconar algo a lista para poder ultilizar o desfazer.')

        elif opcao == 4:
            print('termine sua lista anterior antes de escrever uma nova.\n'
            'pois ao finalizar o programa a lista que tá sendo criada ira sobreescrever\n'
            'a lista anterior já salva.')            
            arquivo_C_lista = 'lista_de_tarefas.json'
            with open(arquivo_C_lista, 'w') as arquivo_salvo:
                json.dump(lista_de_tarefas, arquivo_salvo)

            print(f'Antes de sair. Sua lista é essa {lista_de_tarefas}')

            sair = input('Aperte qualquer tecla para confimar a finalização do programa:')
            print('programa finalizado')
            break
    except ValueError:
        print('Digite um número que corresponde a o que quer fazer.')