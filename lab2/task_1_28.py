from math import log10, log, log2, cos, sin, atan
from prettytable import PrettyTable

def func_one(x):
  return log10(log(x) + log2(x))

def func_two(x):
  return (cos(x)**2 + (cos(x)/sin(x)))**(1/4)

def func_three(x):
  return atan(1/x)

def func_main(h, a, b):
  end_range_one = 2.2
  end_range_two = 3

  result_table = PrettyTable()
  result_table.field_names = ["function", "x", "f(x)"]
  x = a
  while(x <= b):
    if x < end_range_one:
      result_table.add_row(["func_one", x, func_one(x)])
    elif x >= end_range_one and x < end_range_two:
      result_table.add_row(["func_two", x, func_two(x)])
    else:
      result_table.add_row(["func_three", x, func_three(x)])
    x = round(x + h, 2)
  return result_table

result = func_main(0.05, 1.5, 3.5)
print(result)

