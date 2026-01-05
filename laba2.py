def greet(name,old):
    print(f"Привет, {name}! тебе {old}")
greet("НА", "17")

def square(number):
    return number * number * number
rezult = square(5)
print(rezult)

def chet(chislo):
   if chislo % 2 == 0:
      return True
   else:
      return False
rezult = chet(89)
print(rezult)

def summa(chislo, chislo2):
    return chislo + chislo2
i = summa(1,3)
print(i)

def rub(forma):
    return f'{forma}руб'
i = rub(100)
print(i)

def max_of_two(ch, ch2):
    if ch > ch2:
     return ch
    else:
       return ch2
i = max_of_two(5,2)
print(i)

import math
def prosto(chislo):
    if chislo < 2:
        return False
    if chislo == 2:
        return True
    if chislo % 2 == 0:
        return False
    
    for i in range(3, math.isqrt(chislo) + 1, 2):
        if chislo % i == 0:
            return 'составное'
    return True    
i = prosto(27)
print(i)