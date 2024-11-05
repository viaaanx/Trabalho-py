cpf_enviado = input('Informe o respectivo CPF: ') \
    .replace('.', '') \
    .replace('-', '') \
    .replace(' ', '')
nove_digitos = cpf_enviado[:9]
contador_1 = 10

soma_1 = 0
for digito in nove_digitos:
    soma_1 += int(digito) * contador_1
    contador_1 -= 1
digito_1 = (soma_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0
#---------------
dez_digitos = cpf_enviado[0:10]
contador_2 = 11

soma_2 = 0
for digito in dez_digitos:
    soma_2 += int(digito) * contador_2
    contador_2 -= 1
digito_2 = (soma_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado == cpf_calculo:
    print(f'{cpf_enviado} é válido.')
    
else:
    print('CPF Inválido')

