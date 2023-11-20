""" Sorteador de números
Objetivo: criar um sorteador de números com a biblioteca 'random', desta forma, números randômicos são apresentados em uma faixa especificada anteriormente.
Tratamento de erros: se os números informados forem invertidos, os números são sorteados da mesma maneira. """

import random

def number_draw(in_range: int, fi_range: int) -> int:
    if in_range > fi_range: return random.randrange(in_range, fi_range - 1, -1)
    return random.randrange(in_range, fi_range + 1)

if __name__ == '__main__':
    print(number_draw(100, 1100))
    print(number_draw(5, 15))
    print(number_draw(0, 100))
    print(number_draw(100, 5))
    print(number_draw(20, 51))

