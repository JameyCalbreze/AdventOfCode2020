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

  # Where we're standing
  w_x = 10  # initial condition from problem 2
  w_y = 1

  s_x = 0  # Ship is originally at 0,0
  s_y = 0

  for directive in directives:
    command, degree = directive
    if command == "R":
      for _ in range(int(degree/90)%4):
        w_x, w_y = w_y, w_x * -1
    elif command == "L":
      for _ in range(int(degree/90)%4):
        w_x, w_y = w_y * -1, w_x
    elif command == "F":
      s_x += w_x * degree
      s_y += w_y * degree
    else:
      change_x, change_y = movements[command]
      w_x += change_x * degree
      w_y += change_y * degree

  return abs(s_x) + abs(s_y)

if __name__ == "__main__":
  input_file = open("input.txt", "r")
  rows = input_file.readlines()
  trimmed_rows = list()
  for row in rows:
    trimmed_rows.append(row[:-1])
  print("Manhattan distance: {}".format(solve(trimmed_rows)))
  
