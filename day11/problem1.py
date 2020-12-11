import io
import time

def print_board(chairs, num_rows, num_cols):
  print("-" * num_cols)
  for row_num in range(num_rows):
    cur_row = list()
    for col_num in range(num_cols):
      key = (row_num, col_num)
      if key in chairs:
        if chairs[key] == 1:
          cur_row.append('#')
        else:
          cur_row.append('L')
      else:
        cur_row.append('.')
    print("".join(cur_row))



def solve(rows):
  chairs = dict()
  dead_cell = set()

  num_rows = len(rows)
  num_cols = len(rows[0])

  # Register all locations
  for row_num in range(num_rows):
    for col_num in range(num_cols):
      if rows[row_num][col_num] == 'L':
        chairs[(row_num, col_num)] = 0
      else:
        dead_cell.add((row_num, col_num))

  # Let the passengers board
  changed = True
  while changed:
    changed = False
    new_chairs = dict()
    for key in chairs:
      row_num, col_num = key
      num_adj = 0 # init count of number of adjacent people
      for check_row in range(row_num-1, row_num+2): # Check the entire 3 by 3 square
        for check_col in range(col_num-1, col_num+2):
          check_key = (check_row, check_col)
          if key == check_key: # ignore the chair in question
            continue
          elif check_key in chairs: # We're only concerned with actual seats
            num_adj += chairs[check_key] # Add the value of the previous seat
      
      new_chairs[key] = chairs[key] # Copy the unmodified value
      if num_adj == 0: # If no one is sitting near by the seat becomes active
        new_chairs[key] = 1
      elif num_adj > 3: # if four or more people are sitting near by the seat becomes empty
        new_chairs[key] = 0
      changed = changed or chairs[key] != new_chairs[key] # Check if we've encountered a change

    chairs = new_chairs # Swap out the chairs index
    print_board(new_chairs, num_rows, num_cols)

  num_occupied = 0
  for key in chairs:
    num_occupied += chairs[key] # Count all of the occupied seats

  return num_occupied

if __name__ == "__main__":
  input_file = open("input.txt", "r")
  rows = input_file.readlines()
  trimmed_rows = list()
  for row in rows:
    trimmed_rows.append(row[:-1])
  print("Final number of occupied seats: {}".format(solve(trimmed_rows)))
