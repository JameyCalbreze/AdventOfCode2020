import io

def check_row(position, row):
  return row[position % len(row)] == '#'

def solve(rows, increment, row_increment):
  tree_count = 0
  position = 0
  index = 0
  while index < len(rows):
    row = rows[index]
    tree_count += check_row(position, row)
    position += increment
    index += row_increment
  return tree_count

if __name__ == "__main__":
  input_file = open("input.txt", "r", encoding="utf-8")
  rows = input_file.readlines()
  trimmed_rows = list()
  for row in rows:
    trimmed_rows.append(row[:-1])
  solution_1 = solve(trimmed_rows, 1, 1)
  solution_2 = solve(trimmed_rows, 3, 1)
  solution_3 = solve(trimmed_rows, 5, 1)
  solution_4 = solve(trimmed_rows, 7, 1)
  solution_5 = solve(trimmed_rows, 1, 2)
  print("Solution: {}".format(solution_1 * solution_2 * solution_3 * solution_4 * solution_5))
