import os 

lista = []
while True:
    print('Selecione uma opção')
    opcao = input('[I]nserir [A]pagar [L]istar: ').upper()
    
    if opcao == 'I':
        os.system('cls')
        inserir = input('Produto: ').capitalize()
        lista.append(inserir)
        print('Produto adicionado à lista.')
    
    elif opcao == 'A':
        os.system('cls')
        apagar_str = input('Escolha um índice para apagar: ')
        
        try:
            indice = int(apagar_str)
            del lista[indice]
            print('Produto apagado da lista.')
            
        except ValueError:
            print('Por favor digite um número inteiro.')
            print('-=-' *10)
        except IndexError:
            print('Índice não existente na lista')
            print('-=-' *10)
        except Exception:
            print('Erro desconhecido')
            print('-=-' *10)
            
    elif opcao == 'L':
        os.system('cls')
       
        if lista == []:
            print('Não há oque listar.')
            
        for indice, nome in enumerate(lista):
            print(f'{indice} - {nome}')
            
    else:
        os.system('cls')
        print('Selecione uma opção válida.')
            
    
            