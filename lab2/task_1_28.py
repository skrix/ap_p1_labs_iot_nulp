import math
from prettytable import PrettyTable

def func_one(x):
  return math.log10(math.log(x) + math.log2(x))

def func_two(x):
  return (math.cos(x)**2 + (math.cos(x)/math.sin(x)))**(1/4)

def func_three(x):
  return math.atan(1/x)

def func_main(h, a, b):
  result_table = PrettyTable()
  result_table.field_names = ["function", "x", "f(x)"]
  x = a
  while(x <= b):
    if x < 2.2:
      result_table.add_row(["func_one", x, func_one(x)])
    elif x >= 2.2 and x < 3:
      result_table.add_row(["func_two", x, func_two(x)])
    else:
      result_table.add_row(["func_three", x, func_three(x)])
    x = round(x + h, 2)
  return result_table

result = func_main(0.05, 1.5, 3.5)
print(result)

