import io
import math

def solve(rows):
  depart_time = int(rows[0])
  buses = rows[1].split(',')
  
  bus_to_leave = -1
  min_wait = math.inf
  for bus in buses:
    if bus == 'x':
      continue
    bus_i = int(bus)
    wait_time = bus_i - (depart_time % bus_i)
    if wait_time == bus_i:
      wait_time = 0
    if wait_time < min_wait:
      min_wait = wait_time
      bus_to_leave = bus_i

  return bus_to_leave * min_wait

if __name__ == "__main__":
  input_file = open("input.txt","r")
  rows = input_file.readlines()
  trimmed_rows = list()
  for row in rows:
    trimmed_rows.append(row[:-1])
  print("Solution: {}".format(solve(trimmed_rows)))
