import os

def solve(rows):
  rows.append(0) # Append the outlet
  rows.sort()
  rows.append(rows[-1] + 3) # Append the laptop dif

  num_1 = 0
  num_3 = 0
  pos = 0
  while pos != len(rows)-1:
    dif = rows[pos+1] - rows[pos]
    if dif == 1:
      num_1 += 1
    elif dif == 3:
      num_3 += 1
    pos += 1

  return num_1 * num_3

if __name__ == "__main__":
  input_file = open("input.txt", "r")
  rows = input_file.readlines()
  trimmed_rows = list()
  for row in rows:
    trimmed_rows.append(int(row))
  print("Solution: {}".format(solve(trimmed_rows)))
