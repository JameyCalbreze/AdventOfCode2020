import io

def check_row(position, row):
  return row[position % len(row)] == '#'

def solve(rows):
  tree_count = 0
  position = 0
  for row in rows:
    tree_count += check_row(position, row)
    position += 3
  return tree_count

if __name__ == "__main__":
  input_file = open("input.txt", "r", encoding="utf-8")
  rows = input_file.readlines()
  trimmed_rows = list()
  for row in rows:
    trimmed_rows.append(row[:-1])
  print("Number of trees encountered: {}".format(solve(trimmed_rows)))
