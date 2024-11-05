"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
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

