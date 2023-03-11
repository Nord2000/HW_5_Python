"""
Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
"""
q = int(input('Введите число A '))
w = int(input('Введите число B '))
def degree(q,w):
    if w == 0:
        return 1
    return q * degree(q, w - 1)
print(degree(q,w))


2