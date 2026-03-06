from documentos import (cadastrar_documento, listar_documentos, buscar_documento, atualizar_documento, remover_documento)
from auxiliar import (finalizar_sistema, opcao_invalida, voltar_ao_menu)

def exibir_menu_sistema():
    print('S̲i̲s̲t̲e̲m̲a̲ d̲e̲ C̲o̲n̲t̲r̲o̲l̲e̲ d̲e̲ D̲o̲c̲u̲m̲e̲n̲t̲o̲s̲\n')
    print('1. Cadastrar documento')
    print('2. Listar documentos')
    print('3. Buscar documento por ID')
    print('4. Atualizar documento')
    print('5. Remover documento')
    print('6. Sair\n')

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_documento()
        elif opcao_escolhida == 2:
            listar_documentos()
        elif opcao_escolhida == 3:
            buscar_documento()
        elif opcao_escolhida == 4:
            atualizar_documento()
        elif opcao_escolhida == 5:
            remover_documento()
        elif opcao_escolhida == 6:
            finalizar_sistema()
    except ValueError:
        opcao_invalida()
        