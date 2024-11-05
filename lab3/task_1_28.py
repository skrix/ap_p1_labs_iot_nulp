def index_of_impostor(array):
  length = len(array) + 1
  if sum(array) == 0:
    return 0
  else:
    i = 0
    while (i < length):
      if (sum(array[0:i]) == sum(array[i+1:length])):
        return i
      else:
        i += 1

test_array = [1,2,3,4,3,2,1]
index = index_of_impostor(test_array)
print(f"Index of impostor is {index} and it's number {test_array[index]}")
