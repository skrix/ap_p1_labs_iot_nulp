import math
from prettytable import PrettyTable

def func_one(x, k):
  return ((-1)**(k+1) * math.cos(k * x))/((x + 2*k)**3)

def func_two(x, d):
  k = 1
  sum = 0
  while abs(func_one(x, k)) > d:
      sum += func_one(x, k)
      k += 1
  return sum

def func_main(h, a, b, d):
  result_table = PrettyTable()
  result_table.field_names = ["x", "f(x)"]
  x = a
  while(x <= b):
    result_table.add_row([x, func_two(x, d)])
    x = round(x + h, 2)
  return result_table

result = func_main(0.1, 1.5, 3.5, 0.001)
print(result)

