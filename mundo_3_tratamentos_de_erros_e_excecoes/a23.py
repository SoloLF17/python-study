try:
    a = int(input('Digite um numero: '))
    b = int(input('Digite um numero: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possivel dividir por um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados')
except Exception as erro:
    print(f'O erro encontrado foi de {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre.')