import os
from datetime import datetime
from auxiliar import (exibir_subtitulo, voltar_ao_menu, sinalizar_sem_documento, entrada_vazia)

documentos = []
gerador_id = 1

def cadastrar_documento():
    global gerador_id
    data_doc = None
    exibir_subtitulo('Cᴀᴅᴀsᴛʀᴏ ᴅᴇ ᴅᴏᴄᴜᴍᴇɴᴛᴏs')
    nome_doc = input('Digite o nome do documento: ')
    tipo_doc = input('Digite o tipo do documento: ')
    data = input('Digite a data do documento (DDMMAAAA): ')
    if not nome_doc or not tipo_doc or not data:
        entrada_vazia()
        return
    try:
        data_doc = datetime.strptime(data, '%d%m%Y').date()
    except ValueError:
        print("\nData inválida!")
        voltar_ao_menu()
        return
    documento = {'id' : gerador_id, 'nome' : nome_doc.title(), 'tipo' : tipo_doc.upper(), 'data' : data_doc}
    documentos.append(documento)
    print(f'\nO documento "{nome_doc.title()}" foi cadastrado com o id {gerador_id}!\n')
    gerador_id += 1
    voltar_ao_menu() 

def listar_documentos():
    if not documentos:
        sinalizar_sem_documento()
    else:
        exibir_subtitulo('Lɪsᴛᴀ ᴅᴇ ᴅᴏᴄᴜᴍᴇɴᴛᴏs')
        for documento in documentos:
            nome_doc = documento['nome']
            id_doc = documento['id']
            tipo_doc = documento['tipo']
            print(f'- ID: {id_doc} | Documento: {nome_doc} | Tipo: {tipo_doc} | Data: {documento['data'].strftime('%d/%m/%Y')}')
        voltar_ao_menu()
    
def buscar_documento():
    if not documentos:
        sinalizar_sem_documento()
    else:
        exibir_subtitulo('Bᴜsᴄᴀ ᴅᴇ ᴅᴏᴄᴜᴍᴇɴᴛᴏs')
        try:
            id_busca = int(input('Digite o ID do documento que busca: '))
            encontrado = False
            for documento in documentos:
                if id_busca == documento['id']:
                    print(f'- ID: {id_busca} | Documento: {documento["nome"]} | Tipo: {documento["tipo"]} | Data: {documento['data'].strftime('%d/%m/%Y')}')
                    encontrado = True
                    voltar_ao_menu()
                    break
            if not encontrado:
                    print('ID inválido!')
                    voltar_ao_menu()
        except ValueError:
            os.system('cls')
            print("ID inválido!")
            voltar_ao_menu()

def remover_documento():
    if not documentos:
        sinalizar_sem_documento()
    else:
        exibir_subtitulo('Rᴇᴍᴏᴠᴇʀ ᴅᴏᴄᴜᴍᴇɴᴛᴏs')
        try:
            id_remover = int(input('Digite o ID do documento que deseja remover: '))
            encontrado= False
            for documento in documentos:
                if id_remover == documento['id']:
                    documentos.remove(documento)
                    print('Documento removido com sucesso!')
                    encontrado = True
                    voltar_ao_menu()
                    break
            if not encontrado:
                    print('ID inválido!')
                    voltar_ao_menu()
        except ValueError:
            os.system('cls')
            print('ID inválido!')
            voltar_ao_menu() 

def atualizar_documento():
    if not documentos:
        sinalizar_sem_documento()
    else:
        exibir_subtitulo('Aᴛᴜᴀʟɪᴢᴀʀ ᴅᴏᴄᴜᴍᴇɴᴛᴏs')
        try:
            id_atualizar = int(input('Digite o ID do documento que deseja atualizar: '))
            encontrado = False
            for documento in documentos:
                if id_atualizar == int(documento["id"]):
                    encontrado = True
                    print('Que campo deseja atualizar?')
                    print('1. Nome')
                    print('2. Tipo')
                    print('3. Data\n')
                    atualizar_doc = int(input('Escolha uma opção: '))
                    if atualizar_doc == 1:
                        nome_novo = input('Digite o novo nome: ')
                        documento['nome'] = nome_novo.title()
                        print(f'Campo Nome alterado para "{documento["nome"]}" com sucesso!\n')
                        voltar_ao_menu()
                    elif atualizar_doc == 2:
                        tipo_novo = input('Digite o novo tipo: ')
                        documento['tipo'] = tipo_novo.upper()
                        print(f'Campo Tipo alterado para "{documento["tipo"]}" com sucesso!\n')
                        voltar_ao_menu()
                    elif atualizar_doc == 3:
                        data_atualizada = None
                        data_nova = input('Digite a nova data: ')
                        try:
                            data_atualizada = datetime.strptime(data_nova, '%d%m%Y').date()
                        except ValueError:
                            print("\nData inválida!")
                        documento['data'] = data_atualizada
                        print(f'Campo Data alterado para "{documento['data'].strftime('%d/%m/%Y')}" com sucesso!\n')
                        voltar_ao_menu()
                    else:     
                        os.system('cls')
                        print('Opção inválida!')
                        voltar_ao_menu()
                    break
            if not encontrado:
                    os.system('cls')
                    print('ID inválido!')  
                    voltar_ao_menu()      
        except ValueError:
            os.system('cls')
            print('ID inválido!')  
            voltar_ao_menu()