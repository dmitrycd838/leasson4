# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.
#     Обратите внимание, что создаваемый цикл не должен быть бесконечным.
#     Необходимо предусмотреть условие его завершения.
from itertools import count, cycle
import sys

start_from = 10
iterable = "GSYWVZJA"
iterations_count = 0

def integer_generator(start_from):
    for el in count(start_from):
        if el > start_from+100:
            break
        yield el

for el in integer_generator(10):
    print(el)

# gen = integer_generator(10)
# print(gen)
# print(sys.getsizeof(gen))
# print(sys.getsizeof(list(gen)))

for el in cycle(iterable):
    if el == iterable[0]:
        iterations_count += 1
    if iterations_count < 3:
        print(el)
    else:
        break
        
