import io

def solve(rows):
  directives = list()
  for row in rows:
    directives.append((row[0], int(row[1:])))

  movements = dict()
  movements["N"] = (0, 1)
  movements["E"] = (1, 0)
  movements["S"] = (0, -1)
  movements["W"] = (-1, 0)
  cardinals = ("N", "E", "S", "W")
  facing = 1

  # Where we're standing
  x = 0
  y = 0

  for directive in directives:
    command, degree = directive
    change_x = 0
    change_y = 0
    if command == "R":
      facing = int((facing + (degree/90)) % 4)
    elif command == "L":
      facing = int((facing + 4 - (degree/90)) % 4)
    elif command == "F":
      change_x, change_y = movements[cardinals[facing]]
    else:
      change_x, change_y = movements[command]
    x += change_x * degree
    y += change_y * degree

  return abs(x) + abs(y)

if __name__ == "__main__":
  input_file = open("input.txt", "r")
  rows = input_file.readlines()
  trimmed_rows = list()
  for row in rows:
    trimmed_rows.append(row[:-1])
  print("Manhattan distance: {}".format(solve(trimmed_rows)))
  
