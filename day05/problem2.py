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
  all_seat_ids = list()
  for row in rows:
    row_seek = row[:7]
    col_seek = row[7:]

    row_num = solve_row(0, 127, row_seek)
    col_num = solve_col(0, 7, col_seek)
  
    all_seat_ids.append((row_num * 8) + col_num)
    
  all_seat_ids.sort()
  pos = 0
  while all_seat_ids[pos] + 1 == all_seat_ids[pos + 1]:
    pos += 1

  return all_seat_ids[pos] + 1

if __name__ == "__main__":
  input_file = open("input.txt", "r")
  rows = input_file.readlines()
  trimmed_rows = list()
  for row in rows:
    trimmed_rows.append(row[:-1])
  print("My seat id: {}".format(solve(trimmed_rows)))
  