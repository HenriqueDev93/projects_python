""" Calculadora de Índice de Massa Corporal
Objetivo: criar uma calculadora IMC
Source: https://alice.com.br/blog/sua-saude/como-calcular-imc/ """

def imc_calculator(user_height: float, user_weight: float) -> str:
    user_imc: float = round(user_weight / (user_height**2), 2)
    show_imc: str = str(user_imc).replace('.', ',')

    """ coleta e tratamento dos dados """

    if user_imc > 0 and user_imc < 18.5:
        return f'Você está abaixo do peso! Seu IMC é de {show_imc}'
    elif user_imc > 18.5 and user_imc < 25:
        return f'Você está no peso ideal! Seu IMC é de {show_imc}'
    elif user_imc >= 25 and user_imc < 30:
        return f'Você está com sobrepeso! Seu IMC é de {show_imc}'
    elif user_imc >= 30 and user_imc < 35:
        return f'Você está com Obesidade I (nível 1)! Seu IMC é de {show_imc}'
    elif user_imc >= 35 and user_imc < 40:
        return f'Você está com Obesidade II (nível 2)! Seu IMC é de {show_imc}'
    elif user_imc >= 40 and user_imc < 100:
        return f'Você está com Obesidade III (nível 3)! Seu IMC é de {show_imc}'
    else:
        return 'Valor inválido, tente novamente.'

if __name__ == '__main__':

    try:
        user_height = float((input('Qual sua altura? ') + '00').replace(',', '').replace('.', '')[0:3])/100
        user_weight = float(input('Qual seu peso? ').replace(',', '.'))

        print(imc_calculator(user_height, user_weight))

    except:
        print('Valores inseridos inválidos, tente novamente.')