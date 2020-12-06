import io

def solve(rows):
  count = 0
  cur_set = set()
  first = True
  for row in rows:
    if row == "":
      count += len(cur_set)
      first = True
    else:
      cur_letters = set()
      for letter in row:
        cur_letters.add(letter)
      if first:
        cur_set = cur_letters
        first = False
      else:
        cur_set = cur_set.intersection(cur_letters)
  
  count += len(cur_set)
  return count


if __name__ == "__main__":
  input_file = open("input.txt", "r")
  rows = input_file.readlines()
  trimmed_rows = list()
  for row in rows:
    trimmed_rows.append(row[:-1])
  print("Number of yes among groups: {}".format(solve(trimmed_rows)))
  