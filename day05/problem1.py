import io
import math

def solve_col(start, end, string):
  for char in string:
    mid = int((start+end)/2)
    if char == 'L':
      end = mid
    elif char == 'R':
      start = mid+1
  return start

def solve_row(start, end, string):
  for char in string:
    mid = int(math.floor((start+end)/2))
    if char == 'F':
      end = mid
    elif char == 'B':
      start = mid+1
  return start

def solve(rows):
  max_seat_id = -1
  for row in rows:
    row_seek = row[:7]
    col_seek = row[7:]

    row_num = solve_row(0, 127, row_seek)
    col_num = solve_col(0, 7, col_seek)
  
    seat_id = (row_num * 8) + col_num
    if seat_id > max_seat_id:
      max_seat_id = seat_id

  return max_seat_id

if __name__ == "__main__":
  input_file = open("input.txt", "r")
  rows = input_file.readlines()
  trimmed_rows = list()
  for row in rows:
    trimmed_rows.append(row[:-1])
  print("Max seat id: {}".format(solve(trimmed_rows)))
  