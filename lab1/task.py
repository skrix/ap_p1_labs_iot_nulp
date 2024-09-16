import requests

url = "https://raw.githubusercontent.com/skrix/cv/main/cv.tex"
response = requests.get(url)
print(response.text)

game = "Sleeping Dogs"
print(game)

is_student = False
is_teacher = True
print(is_student and is_teacher)
print(is_student or is_teacher)

is_raining = False
is_snowing = False
print(not is_raining)
print(not is_snowing)

x = 1.22
y = 3.21
result = (x * y)**(1/3) + 13 * (x - y)**4 - x/y
print(result)
