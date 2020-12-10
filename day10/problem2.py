import os

def count_permutations(rows, index, prev_val, cache_dict):
  if index == len(rows):
    return 0 # Base case

  key = (prev_val, tuple(rows[index:]))
  if key in cache_dict:
    return cache_dict[key]

  permutations = 0
  if (rows[index] - prev_val) <= 3:
    if index == len(rows)-1:
      permutations = 1
    permutations += count_permutations(rows, index + 1, prev_val, cache_dict) # The permutations with the current index ignored
    permutations += count_permutations(rows, index + 1, rows[index], cache_dict) # The permutations with the current index acknowledged

  # print("Calls: {}, Permutations: {}, Index: {}, Previous Value: {}".format(count_calls, permutations, index, prev_val))

  cache_dict[key] = permutations

  return permutations

def solve(rows):
  rows.sort()
  rows.append(rows[-1] + 3) # Append the laptop dif
  cache_dict = dict()
  hold = count_permutations(rows, 0, 0, cache_dict)
  for key in cache_dict:
    print("Key: {}, Val: {}".format(key, cache_dict[key]))
  return hold

if __name__ == "__main__":
  input_file = open("input.txt", "r")
  rows = input_file.readlines()
  trimmed_rows = list()
  for row in rows:
    trimmed_rows.append(int(row))
  print("Solution: {}".format(solve(trimmed_rows)))
