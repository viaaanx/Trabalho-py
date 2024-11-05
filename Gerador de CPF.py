import random
quantidade = int(input("Quantos CPF'S deseja gerar? "))
print('Deseja gerar com pontuação?')
pont = input('[S]im [N]ão ').upper()

for _ in range(quantidade):
    nove_digitos = ''
    for indice in range(9):
        nove_digitos += str(random.randint(0, 9))
    contador_1 = 10

    soma_1 = 0
    for digito in nove_digitos:
        soma_1 += int(digito) * contador_1
        contador_1 -= 1
    digito_1 = (soma_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0
  
    dez_digitos = nove_digitos + str(digito_1)
    contador_2 = 11

    soma_2 = 0
    for digito in dez_digitos:
        soma_2 += int(digito) * contador_2
        contador_2 -= 1
    digito_2 = (soma_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_calculo = f'{nove_digitos}{digito_1}{digito_2}'
    
    if pont == 'S':
       cpf_calculo = '{}.{}.{}-{}'.format(cpf_calculo[:3], cpf_calculo[3:6], cpf_calculo[6:9], cpf_calculo[9:])
       print(cpf_calculo)
           
    else:
        print(cpf_calculo)