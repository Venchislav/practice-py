# mine
def sort_array(source_array):
    for i in range(0, len(source_array)):
        for j in range(i, len(source_array)):
            if(source_array[i] % 2 == 1 and source_array[j] % 2 == 1):
                if(source_array[j] < source_array[i]):
                    aux = source_array[i]
                    source_array[i] = source_array[j]
                    source_array[j] = aux
    return source_array

# shorter

def sort_array(arr):
  odds = sorted((x for x in arr if x%2 != 0), reverse=True)
  return [x if x%2==0 else odds.pop() for x in arr]
