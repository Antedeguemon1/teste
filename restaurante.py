import os
restaurantes=[{"nome": "𝕔𝕒𝕓𝕖𝕔̧𝕒 𝕕𝕖 𝕘𝕖𝕝𝕠", "categoria": "almoço", 'ativo':True},
              {"nome": "WWII", "categoria":"lanches", "ativo":False},
              {"nome": "TI", 'categoria':"bar", "ativo":False}]

def exibir_nome_do_programa():
    '''essa função exibe o nome do restaurante'''
  
    print("𝕔𝕒𝕓𝕖𝕔̧𝕒 𝕕𝕖 𝕘𝕖𝕝𝕠")
    
def exibir_opções():

    '''essa função exibe as opções'''
    print("1-cadastrar restaurante")
    print("2-listar restaurante")
    print("3-alterar status do restaurante") 
    print("4-encerrar programa")
       
def Encerrando_programa():
    '''essa função encerra o programa'''
    exibir_subtitulo("encerrando programa")
    voltar_ao_menu_principal()
    
def opção_invalida():
    '''essa função volta ao menu se for opção inválida'''
    print('Opção invalida"!\n')
    voltar_ao_menu_principal()

def cadastrar_novo_restaurante():

    '''essa função cadastra um novo restaurante'''
    exibir_subtitulo("cadastrando novo restaurante")
    nome_do_restaurante = input('digite o nome do restaurante que deseja cadastrar: ')
    categoria = input (f'digite a categoria do restaurante {nome_do_restaurante} ')
    dados_do_restaurante ={"nome": nome_do_restaurante,"categoria":categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'o restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def voltar_ao_menu_principal():
      
      '''essa função volta ao menu principal'''
      input("\nDigite qualquer tecla para voltar ao menu principal")
      main()
    
def alternar_estado_do_restaurante():

    '''essa função alterna o estado do restaurante'''
    exibir_subtitulo('alterando estado do restaurante')
    nome_restaurante = input('digite o nome do restaurante que deseja alterar  o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
         if nome_restaurante == restaurante['nome']:
              restaurante_encontrado = True
              restaurante['ativo'] = not restaurante ['ativo']
              mensagem = f'o restaurante {nome_restaurante} foi ativado com sucesso' if restaurante ["ativo"]else f'o restaurante{nome_restaurante} foi desativado com sucesso'
              print (mensagem)
    if not restaurante_encontrado:
         print('o restaurante não foi encontrado')

    voltar_ao_menu_principal()

def listar_restaurantes():

    '''essa função lista os restaurantes'''
    exibir_subtitulo("listando restaurantes")

    
    for restaurante in restaurantes:
        nome_restaurante=restaurante['nome']
        categoria = restaurante["categoria"]
        status = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f' - .{nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {status.ljust(20)}')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):

    '''essa função exibe os subtitulos'''
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def escolher_opção():

    '''essa função serve para esccolher as opções disponiveis'''
    try:
       
        opção = int(input("escolha uma opção:"))
        print('a opção escolhida foi:',opção)



        if opção == 1:
                cadastrar_novo_restaurante()
        elif opção == 2:
              listar_restaurantes()
        elif opção == 3:
                alternar_estado_do_restaurante()
        elif opção == 4:
                Encerrando_programa()
        else:
                opção_invalida()
    except:
          
          opção_invalida()
def main():
        
        '''essa função inicia o programa'''
        os.system('cls')
        exibir_nome_do_programa()
        exibir_opções()
        escolher_opção()

if __name__ == '__main__':
    main()

